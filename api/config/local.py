from .default import *

usuario = "flask"
nombre_bd = "finanzas_grupales"
contrasenia = r"018168"
bd_type = "mysql+pymysql"
host = "localhost"

SQLALCHEMY_DATABASE_URI = f'{bd_type}://{usuario}:{contrasenia}@{host}/{nombre_bd}'

print(SQLALCHEMY_DATABASE_URI)

APP_ENV = APP_ENV_LOCAL
DEBUG = True