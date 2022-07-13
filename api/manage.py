#############################################################################
#                                                                           #
#                       Copyright 2022 Ammar Akbar                          #
#                           All Rights Reserved.                            #
#                                                                           #
#############################################################################
"""
This file contains the CLI methods for the flask application.

@last_modified: July 09, 2022

@author: Ammar Akbar
"""
from flask.cli import FlaskGroup

from api import APP, DB
from api.utils.constants import COUNTRIES

cli = FlaskGroup(APP)


@cli.command('initialize')
def initialize():
    DB.drop_all()
    DB.create_all()
    DB.session.commit()


@cli.command('insert_user_data')
def insert_user_data():
    countries_len = len(COUNTRIES)
    query = (f"INSERT INTO USERS (Email, Name, Age, Country) SELECT 'user_' || num || '@powertofly.com', "
             f"'User ' || num, FLOOR(RANDOM() * (90-10+1) + 10)::int, "
             f"(ARRAY{COUNTRIES})[floor(random()*{countries_len})+1] "
             f"from generate_series(1, 1000000) as num;")
    DB.session.execute(query)
    DB.session.commit()
