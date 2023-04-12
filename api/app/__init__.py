from flask import Flask, got_request_exception, jsonify
from flask_jwt_extended import JWTManager
from flask_restful import Api
from app.common.error_handling import InvalidAPIUsage, ObjectNotFound, AppErrorBaseClass
from app.common.errors import custom_api_error_handler
from app.db import db

from app.modules.auth.v1.resources import *
from app.modules.categories.v1.resources import categories_bp

from app.ext import ma, migrate
from flask_cors import CORS

def create_app(settings_module = 'config.local'):
   app = Flask(__name__)
   app.config.from_object(settings_module)
   
   # Inicializa las extensiones
   db.init_app(app)
   ma.init_app(app)
   migrate.init_app(app, db)
   jwt = JWTManager(app)
   cors = CORS(app, resources={r'/*': {'origins':'*'}})

   # Captura todos los errores 404
   Api(app, catch_all_404s=True)

   # Deshabilita el modo estricto de acabado de una URL con /
   app.url_map.strict_slashes = False

   # Registra los blueprints
   app.register_blueprint(login)
   app.register_blueprint(categories_bp)

   # Registra manejadores de errores personalizados
   if settings_module != 'config.local':
      got_request_exception.connect(custom_api_error_handler, app)
      register_error_handlers(app)
   return app

def register_error_handlers(app):
   @app.errorhandler(Exception)
   def handle_500_error(e):
      return jsonify({'msg': f'Error: {e}'}), 500

   @app.errorhandler(405)
   def handle_405_error(e):
      return jsonify({'msg': 'Metodo no permitido'}), 405

   @app.errorhandler(403)
   def handle_403_error(e):
      return jsonify({'msg': 'Forbidden error'}), 403

   @app.errorhandler(404)
   def handle_404_error(e):
      return jsonify({'msg': 'URL no encontrada'}), 404

   @app.errorhandler(AppErrorBaseClass)
   def handle_app_base_error(e):
      return jsonify({'msg': str(e)}), 500
      
   @app.errorhandler(ObjectNotFound)
   def handle_object_not_found_error(e):
      return jsonify({'msg': str(e)}), 404