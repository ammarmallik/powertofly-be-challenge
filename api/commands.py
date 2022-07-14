#############################################################################
#                                                                           #
#                       Copyright 2022 Ammar Akbar                          #
#                           All Rights Reserved.                            #
#                                                                           #
#############################################################################
"""
This file contains the CLI methods for the flask application.

@last_modified: July 14, 2022

@author: Ammar Akbar
"""
from flask import Blueprint

from api import DB
from api.utils.constants import COUNTRIES

CLI = Blueprint('cli', __name__)


@CLI.cli.command('init_db')
def initialize():
    DB.drop_all()
    DB.create_all()
    DB.session.commit()


@CLI.cli.command('seed_db')
def insert_user_data():
    countries_len = len(COUNTRIES)
    query = (f"INSERT INTO USERS (Email, Name, Country) SELECT 'user_' || num || '@powertofly.com', "
             f"'User ' || num, (ARRAY{COUNTRIES})[floor(random()*{countries_len})+1] "
             f"from generate_series(1, 1000000) as num;")
    DB.session.execute(query)
    DB.session.commit()
