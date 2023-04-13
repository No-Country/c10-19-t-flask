from flask_jwt_extended import create_access_token
from flask_restful import Api, Resource
from marshmallow import ValidationError
from app.modules.members.v1.schemas import UserSchema
from app.modules.models import User #from app.models import User

from flask import Blueprint, request
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests
from datetime import timedelta
import uuid


login = Blueprint('login', __name__)
api = Api(login)

user_schema = UserSchema()

class Login(Resource):
    def post(self):
        data = request.get_json()
        try:
            data = user_schema.load(data)
        except ValidationError as err:
            return {'error': err.messages}
        user = User.find_by_email(data['email']) # type: ignore
        if user and user.verify_password(data['password']): # type: ignore
            access_token = create_access_token(identity=user.id)
            return {'access_token': access_token, 'user': user_schema.dump(user)}, 200
        return {'message': 'Invalid credentials'}, 401

class SignUp(Resource):
    def post(self): 
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if email is None or password is None:
            return {'message': 'parametros incorrectos'}, 401
        user = User(email=email, password=password)
        user.save()

        return {'message': 'usuario creado con exito'}

class SocialLogin(Resource):
    def post(self):
        args = request.get_json()
        social_type = args.get('social_type')
        token = args.get('token')
        try:
            if social_type == 'google':
                # Verificar el token de Google y obtener la información del usuario
                id_info = id_token.verify_oauth2_token(token, google_requests.Request(), 'google_id')
                if id_info['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                    raise ValueError('Wrong issuer.')
                # Obtener el correo electrónico y el ID de usuario del usuario de Google
                email = id_info['email']
                social_id = id_info['sub']
                # Verificar si el usuario ya ha iniciado sesión con Google en el pasado
                user = User.find_by_social_id(social_id, 'google')
                if not user:
                    # Si es la primera vez que el usuario inicia sesión con Google, crear un nuevo usuario en la base de datos
                    # con un nuevo correo electrónico generado aleatoriamente
                    new_email = str(uuid.uuid4()) + '@example.com'
                    user = User(email=new_email, social_id=social_id, social_type='google')
                    user.save_to_db()
                # Crear un token de acceso JWT para el usuario
                access_token = create_access_token(identity=user.id, expires_delta=timedelta(days=7))
                return {'access_token': access_token}, 200
        except ValueError:
            # Invalid token
            return {'message': 'Invalid token'}, 400
        
api.add_resource(Login, '/api/v1/login', endpoint='login')
api.add_resource(SignUp, '/api/v1/signup', endpoint='signup')
api.add_resource(SocialLogin, '/api/v1/login/social', endpoint='socialLogin')