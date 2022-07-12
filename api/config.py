#############################################################################
#                                                                           #
#                       Copyright 2022 Ammar Akbar                          #
#                           All Rights Reserved.                            #
#                                                                           #
#############################################################################
"""
This file contains all the configurations for the project.

@last_modified: July 09, 2022

@author: Ammar Akbar
"""
import os


class BaseConfig:
    """
    This is the base config class that provides the required configurations for the project.
    """
    POSTGRES_HOST = os.environ.get('POSTGRES_HOST', 'localhost')
    POSTGRES_DB = os.environ.get('POSTGRES_DB', 'powertofly_dev')
    POSTGRES_PORT = os.environ.get('POSTGRES_PORT', 5432)
    POSTGRES_USER = os.environ.get('POSTGRES_USER', 'powertofly')
    POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'powertofly')
    SQLALCHEMY_DATABASE_URI = (f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/'
                               f'{POSTGRES_DB}')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(BaseConfig):
    """
    This class provides development configuration.
    """
    DEBUG = True


class StageConfig(BaseConfig):
    """
    This class provides stage configuration.
    """
    DEBUG = False


class ProdConfig(BaseConfig):
    """
    This class provides production configuration.
    """
    DEBUG = False
