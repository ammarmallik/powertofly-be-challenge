#############################################################################
#                                                                           #
#                       Copyright 2022 Ammar Akbar                          #
#                           All Rights Reserved.                            #
#                                                                           #
#############################################################################
"""
This file is the web server gateway interface.

@last_modified: July 09, 2022

@author: Ammar Akbar
"""
import os

from api import APP
from api.manage import cli


if __name__ == '__main__':
    cli()
    port = int(os.environ.get('PORT', 5000))
    APP.run(host='0.0.0.0', port=port)
