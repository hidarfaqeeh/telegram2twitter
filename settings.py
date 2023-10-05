#!/usr/bin/env python

# https://my.telegram.org/auth and @BotFather

telegram = {'channel': 'Yepoets',  # channel name
        'token': '1329124972:AAFzXynkHxjEWxAXhM-Oil27LzhiTp7YFgw',  # your bot token
        'api_id': 24343527,
        'api_hash': 'c1259b40b2ba148a795f8db4a830cbf5',
        'phone': '+967770440543'}

#get this from https://apps.twitter.com/

twitter = {'consumer_key': 'B5jjnCXSqbn6JqACFnI2zGkP6',
            'consumer_secret': 'PocLgaoQp65krFu2RfzUy0N2JzGPAXYbavos6zqOJVoeVUXB2U',
            'access_token': '1709938703295291392-HphdHxnLXPvc6lPYvlcFDAkzasMeSk',
            'access_token_secret': 'GjYDbOw8KPc1egjIhbjLMNIFXSZYW3TShLXYBEx8cLRlz'}

util = {'start': "2023-10-04 00:00:00",     #date from old posts will be tweeted
        'end': '2023-12-20 00:00:00',       #date until old posts will be tweeted
        'format': '%Y-%m-%d %H:%M:%S',      #date format
        'delay': 0}                         #delay time between tweets for client.py
