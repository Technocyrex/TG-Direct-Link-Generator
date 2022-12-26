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
    BIN_CHANNEL = int(
        ("-1001859320064", None)
    )  # you NEED to use a CHANNEL when you're using MULTI_CLIENT
    PORT = int("PORT", 8080)
    BIND_ADDRESS = str(("WEB_SERVER_BIND_ADDRESS", "0.0.0.0"))
    PING_INTERVAL = int(("PING_INTERVAL", "1200"))  # 20 minutes
    HAS_SSL = ("HAS_SSL", False)
    HAS_SSL = True if str(HAS_SSL).lower() == "true" else False
    NO_PORT = ("NO_PORT", False)
    NO_PORT = True if str(NO_PORT).lower() == "true" else False

    ON_HEROKU = False
    FQDN = '64.227.140.106'
    URL = "http{}://{}{}/".format(
            "s" if HAS_SSL else "", FQDN, "" if NO_PORT else ":" + str(PORT)
        )

    UPDATES_CHANNEL = "null"
    OWNER_ID = int(('OWNER_ID', '1024288582'))

    BANNED_CHANNELS = list(set(int(x) for x in str(("BANNED_CHANNELS", "-1001296894100")).split()))
    BANNED_USERS = list(set(int(x) for x in str(("BANNED_USERS"," 5287015877")).split()))
