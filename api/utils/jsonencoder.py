#############################################################################
#                                                                           #
#                       Copyright 2022 Ammar Akbar.                         #
#                           All Rights Reserved.                            #
#                                                                           #
#############################################################################
"""
This file contains custom JSONEncoder.

@last_modified: July 09, 2022

@author: Ammar Akbar
"""
from datetime import date
from decimal import Decimal

from flask import json
from sqlalchemy.ext.declarative import DeclarativeMeta


class JSONEncoder(json.JSONEncoder):
    """
    Custom JSONEncoder for SQLAlchemy objects.
    """

    def default(self, o):
        """
        Override the default method for JSON encoder.
        :param o: SQLAlchemy object. (object)
        :return: Decoded object. (object)
        """
        if isinstance(o.__class__, DeclarativeMeta):
            data = {}
            fields = o.__json__() if hasattr(o, '__json__') else dir(o)
            for field in [f for f in fields if not f.startswith('_') and f not in ['metadata', 'query', 'query_class']]:
                value = o.__getattribute__(field)
                try:
                    if json.dumps(value):
                        data[field] = value
                except TypeError:
                    data[field] = None
            return data
        elif isinstance(o, Decimal):
            return o.to_eng_string()
        elif isinstance(o, date):
            return o.isoformat()
        return json.JSONEncoder.default(self, o)
