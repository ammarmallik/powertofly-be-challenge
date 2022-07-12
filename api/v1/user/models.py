#############################################################################
#                                                                           #
#                       Copyright 2022 Ammar Akbar                          #
#                           All Rights Reserved.                            #
#                                                                           #
#############################################################################
"""
This file contains models related to `user` module.

@last_modified: July 09, 2022

@author: Ammar Akbar
"""
from api import DB


class User(DB.Model):
    __tablename__ = 'users'

    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(64), unique=True, index=True, nullable=False)
    email = DB.Column(DB.String(64), unique=True, index=True, nullable=False)
    age = DB.Column(DB.Integer, nullable=False, default=18)
    country = DB.Column(DB.String(64), nullable=False, default='Pakistan')
    created_at = DB.Column(DB.DateTime, nullable=False, server_default=DB.func.now())

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __json__(self):
        return {'name': self.name, 'email': self.email, 'age': self.age, 'country': self.country,
                'created_at': self.created_at}
