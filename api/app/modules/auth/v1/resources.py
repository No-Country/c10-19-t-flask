from flask_jwt_extended import create_access_token
from flask_restful import Resource, reqparse
from api.app.modules.models import User #from app.models import User

from flask import request
from flask_restful import Resource
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests
from sqlalchemy.exc import SQLAlchemyError
from datetime import timedelta
import uuid

parser = reqparse.RequestParser()
parser.add_argument('email', help='This field cannot be blank', required=True)
parser.add_argument('password', help='This field cannot be blank', required=True)

class Login(Resource):
    def post(self):
        data = parser.parse_args()
        user = User.find_by_email(data['email'])
        if user and user.password == data['password']:
            access_token = create_access_token(identity=user.id)
            return {'access_token': access_token}, 200
        return {'message': 'Invalid credentials'}, 401

class GoogleLogin(Resource):
    def post(self):
        args = request.get_json()
        token = args.get('token')
        try:
            # Verificar el token de Google y obtener la información del usuario
            id_info = id_token.verify_oauth2_token(token, google_requests.Request(), app.config['GOOGLE_CLIENT_ID'])
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
                try:
                    user.save_to_db()
                except SQLAlchemyError as e:
                    db.session.rollback()
                    return {'message': 'Could not create user'}, 500
            # Crear un token de acceso JWT para el usuario
            access_token = create_access_token(identity=user.id, expires_delta=timedelta(days=7))
            return {'access_token': access_token}, 200
        except ValueError:
            # Invalid token
            return {'message': 'Invalid token'}, 400