#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os
from bots.constants import *

""" Bot Configuration """

app_id = os.environ['APP_ID']
app_pw = os.environ['APP_PW']

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", app_id)
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", app_pw)
