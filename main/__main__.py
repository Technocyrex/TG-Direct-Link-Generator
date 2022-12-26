# This file is a part of TG-Direct-Link-Generator

from os import environ
from dotenv import load_dotenv

load_dotenv()


class Var(object):
    MULTI_CLIENT = False
    API_ID = int("3523181")
    API_HASH = str('78c9a165ba54798fb5e36019397d44ce')
    BOT_TOKEN = str("1609351476:AAGYWE0_jHSDYtPC1uA6MwPvs42spuidWjc")
    SLEEP_THRESHOLD = int('60')
    WORKERS = int("8") 
    BIN_CHANNEL = int("1001859320064")  # you NEED to use a CHANNEL when you're using MULTI_CLIENT
    PORT = int(8080)
    BIND_ADDRESS = str("0.0.0.0")
    PING_INTERVAL = int("1200")  # 20 minutes
    HAS_SSL = False
    #NO_PORT = ("NO_P
    #NO_PORT = True if str(NO_PORT).lower() == "true" else False

    ON_HEROKU = False
    URL = f"http://0.0.0.0:8080"

    UPDATES_CHANNEL = "null"
    OWNER_ID = 1024288582

    BANNED_CHANNELS = list(set(int(x) for x in str(("-1001296894100")).split()))
    BANNED_USERS = list(set(int(x) for x in str(("5287015877")).split()))
