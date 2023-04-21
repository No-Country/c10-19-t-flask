from os.path import abspath, dirname

# Define the application directory
BASE_DIR = dirname(dirname(abspath(__file__)))

SECRET_KEY = "d35bl0que0S"
PROPAGATE_EXCEPTIONS = True
ERROR_404_HELP = False

# Database configuration
SQLALCHEMY_TRACK_MODIFICATIONS = False
SHOW_SQLALCHEMY_LOG_MESSAGES = False

# App environments
APP_ENV_LOCAL = 'local'
APP_ENV_DEVELOPMENT = 'dev'
APP_ENV_PRODUCTION = 'prod'
APP_ENV = ''