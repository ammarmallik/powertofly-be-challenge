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

APP = Flask(__name__)
set_config(APP)
APP.json_encoder = JSONEncoder
DB = SQLAlchemy(APP)

# Import all versions
import api.v1


@APP.route('/', methods=['GET'])
def health():
    """
    Check server health.
    :return: OK. (string)
    """
    return 'OK'
