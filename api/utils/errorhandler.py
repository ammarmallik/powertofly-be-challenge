#############################################################################
#                                                                           #
#                       Copyright 2022 Ammar Akbar.                         #
#                           All Rights Reserved.                            #
#                                                                           #
#############################################################################
"""
This file contains methods related to Werkzeug exceptions handling.

@last_modified: July 13, 2022

@author: Ammar Akbar
"""
from flask import jsonify

DEFAULT_ERRORS = {400: 'REQUEST_ERROR',
                  401: 'UNAUTHORIZED',
                  403: 'FORBIDDEN',
                  404: 'RESOURCE_NOT_FOUND',
                  405: 'METHOD_NOT_ALLOWED',
                  429: 'TOO_MANY_REQUESTS',
                  500: 'INTERNAL_SERVER_ERROR'}


def bad_request(err):
    """
    Handler for all 400 errors.
    :param err: An instance of werkzeug.exceptions. (object)
    :return: HTTP response. (object)
    """
    error = err.description or DEFAULT_ERRORS[400]
    return jsonify(error=error.strip('.')), 400


def resource_not_found(err):
    """
    Handler for all 404 errors.
    :param err: An instance of werkzeug.exceptions. (object)
    :return: HTTP response. (object)
    """
    error = err.description or DEFAULT_ERRORS[404]
    return jsonify(error=error.strip('.')), 404


def method_not_allowed(err):
    """
    Handler for all 405 errors.
    :param err: An instance of werkzeug.exceptions. (object)
    :return: HTTP response. (object)
    """
    error = err.description or DEFAULT_ERRORS[405]
    return jsonify(error=error.strip('.')), 405


def too_many_requests(err):
    """
    Handler for all 429 errors.
    :param err: An instance of werkzeug.exceptions. (object)
    :return: HTTP response. (object)
    """
    error = err.description or DEFAULT_ERRORS[429]
    return jsonify(error=error.strip('.')), 429


def internal_server_error(err):
    """
    Handler for all 500 errors.
    :param err: An instance of werkzeug.exceptions. (object)
    :return: HTTP response. (object)
    """
    error = err.description or DEFAULT_ERRORS[500]
    return jsonify(error=error.strip('.')), 500
