from app.services.user import send_email
from app.serde.user import UserSchema
from app.models.user import User
from app import db


class SignUpView(Resource):
    def post(self):
        data = request.get_json()

        user = User.query.filter(
            func.lower(User.email) == data["email"].strip().lower()
        ).first()

        if user:
            abort(400, "This email address is already in use.")

        user = User()
        user.email = data["email"].strip()
        user.password = data["password"].strip()
        user.last_login = datetime.now()

        db.session.add(user)
        db.session.commit()

        send_email(
            user.email,
            "Account activation",
            "verify_email.html",
            root_domain=request.url_root,
        )

        response = make_response("")
        response.set_cookie(
            "user",
            jwt.encode(
                UserSchema().dump(user), app.config["SECRET_KEY"], algorithm="HS256"
            ),
        )

        return response
    
    from app.services.auth import oauth2_request_uri


class Oauth2SignUpView(Resource):
    def post(self):
        return redirect(
            oauth2_request_uri(request.url_root + "api/users/oauth2callback/signup/")
        )