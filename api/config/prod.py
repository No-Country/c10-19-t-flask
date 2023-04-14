from .default import *
import os

usuario = os.getenv('bd_user')
nombre_bd = "finanzas_grupales"
contrasenia = os.getenv('bd_password')
bd_type = "mysql+pymysql"
host = "localhost"

SQLALCHEMY_DATABASE_URI = f'{bd_type}://{usuario}:{contrasenia}@{host}/{nombre_bd}'

APP_ENV = APP_ENV_LOCAL
DEBUG = False