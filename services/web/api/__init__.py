# -*- coding: utf-8 -*-
"""This module contains initialization code for the api package."""
import os
import sys

from flasgger import LazyJSONEncoder
from flask import Flask

from .blueprints.auth.views import auth
from .blueprints.default.views import default
from .blueprints.extensions import app_logger, db, jwt, swagger
from .error_handlers import handle_bad_request
from .extensions import migrate
from .helpers import are_environment_variables_set, set_flask_environment

if not are_environment_variables_set():
    msg = 'Unable to set Environment variables. Application existing...'
    app_logger.critical(msg)
    sys.exit(1)


def create_app(script_info=None):   # pylint: disable=W0613
    """Create the Flask app."""
    app = Flask(__name__)
    app_logger.info('Successfully created the application instance.')
    app.register_blueprint(default)
    app_logger.info('Successfully registered the default blueprint.')
    app.register_blueprint(auth)
    app_logger.info('Successfully registered the auth blueprint.')

    app.json_encoder = LazyJSONEncoder
    swagger.init_app(app)

    set_flask_environment(app)
    app_logger.info('Successfully set the environment variables.')

    app_logger.info(f"The configuration used is for {os.environ['FLASK_ENV']} environment.")
    app_logger.info(f"The database connection string is {app.config['SQLALCHEMY_DATABASE_URI']}.")

    db.init_app(app=app)
    app_logger.info('Successfully initialized the database instance.')
    migrate.init_app(app, db)
    app_logger.info('Successfully initialized the migrate instance.')
    jwt.init_app(app)
    app_logger.info('Successfully initialized the JWT instance.')

    app.register_error_handler(400, handle_bad_request)
    app_logger.info('Successfully registered te 400 error handler.')

    # shell context for flask cli
    app.shell_context_processor({'app': app, 'db': db})
    return app
