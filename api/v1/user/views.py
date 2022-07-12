#############################################################################
#                                                                           #
#                       Copyright 2022 Ammar Akbar                          #
#                           All Rights Reserved.                            #
#                                                                           #
#############################################################################
"""
This file contains views related to `user` module.

@last_modified: July 09, 2022

@author: Ammar Akbar
"""
from flask import Blueprint, jsonify

from api.v1.user.models import User

BP_USER = Blueprint('user', __name__)


@BP_USER.route('/user', methods=['GET'])
def get_users():
    """
    Retrieve all users based on the given parameters.
    """
    users = User.query.limit(10).all()
    return jsonify({'users': users})
