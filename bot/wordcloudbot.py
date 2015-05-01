import os
import urllib
import tempfile

import fedmsg.config
import fedmsg.meta
import logging.config

import tweepy

# first load the fedmsg config from fedmsg.d
config = fedmsg.config.load_config()

logging.config.dictConfig(config.get('logging'))

fedmsg.meta.make_processors(**config)

topic_filter = 'meetbot.meeting.complete'

consumer_key        = config['consumer_key']
consumer_secret     = config['consumer_secret']
access_token_key    = config['access_token_key']
access_token_secret = config['access_token_secret']

auth_handler = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth_handler.set_access_token(access_token_key, access_token_secret)
twitter_api = tweepy.API(auth_handler)

for name, endpoing, topic, msg in fedmsg.tail_messages():
    if topic_filter not in topic:
        continue

    subtitle = fedmsg.meta.msg2subtitle(msg, **config)
    print subtitle

    link = fedmsg.meta.msg2link(msg, **config)
    title = fedmsg.meta.msg2title(msg, **config)
    cloud = "Fedora_logo.png"

    content = title + " " + link + " " + "#fedora"

    print "Tweeting %r" % content
    twitter_api.update_with_media(cloud, content)
