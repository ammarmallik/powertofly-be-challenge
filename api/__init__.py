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
from flask_sqlalchemy import SQLAlchemy

from api.utils import set_config
from api.utils.jsonencoder import JSONEncoder

DB = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    set_config(app)
    app.json_encoder = JSONEncoder
    DB.init_app(app)

    with app.app_context():
        from api import commands, v1

        app.register_blueprint(commands.CLI)
        app.register_blueprint(v1.views.BP_USER, url_prefix=v1.PREFIX)
        return app


APP = create_app()


@APP.route('/', methods=['GET'])
def health():
    """
    Check server health.
    :return: OK. (string)
    """
    return 'OK'
