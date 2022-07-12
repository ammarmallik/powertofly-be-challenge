#############################################################################
#                                                                           #
#                       Copyright 2022 Ammar Akbar                          #
#                           All Rights Reserved.                            #
#                                                                           #
#############################################################################
"""
Package: `api.v1`

@last_modified: July 09, 2022

@author: Ammar Akbar
"""
from api import APP
from api.v1.user import views
from api.v1.user import models

PREFIX = '/v1'

APP.register_blueprint(views.BP_USER, url_prefix=PREFIX)
