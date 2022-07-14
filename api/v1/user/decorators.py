#############################################################################
#                                                                           #
#                       Copyright 2022 Ammar Akbar                          #
#                           All Rights Reserved.                            #
#                                                                           #
#############################################################################
"""
This file contains decorators for the user APIs.

@last_modified: July 12, 2022

@author: Ammar Akbar
"""
from functools import wraps

from flask import abort, request

from api.utils import constants as c


def parse_request_params(func):
    """
    This function retrieves the parameters from the request.args & request.form.
    @param func: Caller function. (callable)
    @return: Wrapper. (callable)
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        Wrapper function for the parsing the parameters.
        """
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', c.ROWS_PER_PAGE, type=int)
        return_format = request.args.get('format', 'json', type=str)
        if page < 1 or per_page < 1:
            abort(400, 'Page number should be greater than 0')
        if per_page > c.MAX_PER_PAGE:
            abort(400, description=f'Records per page should be less than {c.MAX_PER_PAGE}')
        if return_format not in c.RETURN_FORMATS:
            abort(400, description=f'Unsupported format: {return_format}. It should be from {c.RETURN_FORMATS}')
        try:
            data_filter = request.form['filter']
        except KeyError:
            data_filter = request.args.get('filter')
        kwargs.update({'page': page, 'per_page': per_page, 'format': return_format, 'filter': data_filter})
        return func(*args, **kwargs)
    return wrapper
