#############################################################################
#                                                                           #
#                       Copyright 2022 Ammar Akbar                          #
#                           All Rights Reserved.                            #
#                                                                           #
#############################################################################
"""
This file contains utility methods for the project.

@last_modified: July 09, 2022

@author: Ammar Akbar
"""
import os


def set_config(app):
    """
    Set configuration using the FLASK_ENV environment.
    :param app: Flask App object. (object)
    :return: Flask environment. (str)
    """
    flask_env = os.environ.get('FLASK_ENV')
    config_map = {'development': 'api.config.DevConfig',
                  'stage': 'api.config.StageConfig',
                  'production': 'api.config.ProdConfig'}
    if flask_env not in ['development', 'stage', 'production']:
        flask_env = 'development'
    app.config.from_object(config_map[flask_env])
    return flask_env
