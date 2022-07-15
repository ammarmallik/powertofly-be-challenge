#############################################################################
#                                                                           #
#                       Copyright 2022 Ammar Akbar                          #
#                           All Rights Reserved.                            #
#                                                                           #
#############################################################################
"""
Package: `api`

@last_modified: July 09, 2022

@author: Ammar Akbar
"""
from flask import Flask
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy

from api.utils import set_config

DB = SQLAlchemy()
CACHE = Cache()


def create_app():
    app = Flask(__name__)
    set_config(app)
    DB.init_app(app)
    CACHE.init_app(app)

    with app.app_context():
        from api import commands, v1
        from api.utils import errorhandler as e

        # Clear cache
        CACHE.clear()

        # Register blueprints
        app.register_blueprint(commands.CLI)
        app.register_blueprint(v1.views.BP_USER, url_prefix=v1.PREFIX)

        # Register error handlers
        app.register_error_handler(400, e.bad_request)
        app.register_error_handler(404, e.resource_not_found)
        app.register_error_handler(405, e.method_not_allowed)
        app.register_error_handler(429, e.too_many_requests)
        app.register_error_handler(500, e.internal_server_error)

        return app


APP = create_app()


@APP.route('/', methods=['GET'])
def health():
    """
    Check server health.
    :return: OK. (string)
    """
    return 'OK'
