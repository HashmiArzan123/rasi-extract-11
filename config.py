#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6278216192:AAEKQEI3Zkv1V1bMQYKoFcW-M57OVvX3Znk")
    API_ID = int(os.environ.get("API_ID", "22263567"))
    API_HASH = os.environ.get("API_HASH", "258fb6f6cdfa8220b74a4a6753b2ece6")
    AUTH_USERS = "6446062004"

