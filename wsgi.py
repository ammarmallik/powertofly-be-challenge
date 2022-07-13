#############################################################################
#                                                                           #
#                       Copyright 2022 Ammar Akbar                          #
#                           All Rights Reserved.                            #
#                                                                           #
#############################################################################
"""
This file is the web server gateway interface for Flask App.

@last_modified: July 09, 2022

@author: Ammar Akbar
"""
import os

from api import APP

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
