import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.db import db, BaseModelMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import column_property

class User(db.Model, BaseModelMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    
    # An ID to use as a reference when sending email.
    external_id = db.Column(
        db.String, default=lambda: str(uuid.uuid4()), nullable=False
    )
    
    social_id = db.Column(db.String, nullable=True, unique=True)
    social_type = db.Column(db.String)
    activated = db.Column(db.Boolean, default=False, server_default="f", nullable=False)

    # When the user chooses to set up an account directly with the app.
    _password = db.Column(db.String)

    fullname = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=True)
    picture = db.Column(db.String, nullable=True)

    last_login = db.Column(db.DateTime, nullable=True)

    @property
    def password(self):
        raise AttributeError("Can't read password")

    @password.setter
    def password(self, password):
        self._password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self._password, password)
    
    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_social_id(cls, social_id, social_type):
        return cls.query.filter_by(social_id=social_id, social_type=social_type).first()
