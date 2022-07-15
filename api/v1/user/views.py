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
from flask import Blueprint, jsonify, render_template

from api import CACHE
from api.utils import constants as c
from api.v1.user.decorators import parse_request_params
from api.v1.user.models import User

BP_USER = Blueprint('user', __name__)


@BP_USER.route('/user', methods=['GET', 'POST'])
@parse_request_params
def get_users(**kwargs):
    """
    Retrieve users based on the given parameters.
    :keyword kwargs: Request data. (dict)
        :key page: Page number. (int)
        :key per_page: Total records on a page. (int)
        :key filter: Filter key. (str)
        :key format: Return format e.g. json/html. (str)
    :return: Returns users data based on given format. (object)
    """
    page = kwargs['page']
    per_page = kwargs['per_page']
    return_format = kwargs['format']
    q_filter = kwargs['filter']
    key = f'{page}-{per_page}-{q_filter}-{return_format}'
    if CACHE.has(key):
        return CACHE.get(key)
    users = User.query
    if q_filter:
        search = f'%{q_filter}%'
        users = users.filter(User.email.ilike(search) | User.country.ilike(search))
    users = users.order_by(User.id.asc()).paginate(page=page,
                                                   per_page=per_page,
                                                   max_per_page=c.MAX_PER_PAGE)
    if return_format == 'html' and not CACHE.has(key):
        resp = render_template('powertofly.html', users=users, curr_page=page, per_page=per_page, filter=q_filter)
        CACHE.set(key, resp)
    elif return_format == 'json' and not CACHE.has(key):
        resp = jsonify({
            'curr_page': page,
            'prev_page': users.prev_num if users.has_prev else None,
            'next_page': users.next_num if users.has_next else None,
            'total_pages': users.pages,
            'data': [user.__json__() for user in users.items]
        })
        CACHE.set(key, resp)
    return CACHE.get(key)
