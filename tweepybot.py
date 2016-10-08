from __future__ import unicode_literals
from __future__ import absolute_import, print_function
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import Status
import time
import yaml
from client import slack_client as sc


crontable = []
outputs = []


def broadcast (text):
    for chann in channels:
        outputs.append([chann, text])

class LastTweets:
    """
        Class that maintains an ID for each keyword and broadcast
        it when something new happens
    """
    def __init__(self, api):
        self.api = api
        self.keywords = []
        self.lastid = dict()

    def get_lastid (self,keyword):
    """ Get the last tweet id for a specific keyword """
        if not (keyword in self.lastid):
            search = api.search (keyword, rpp = 1)
            if len(search.ids()) > 0:
                self.lastid[keyword] = search[0].id
            else:
                self.lastid[keyword] = 0
        return self.lastid[keyword]

    def get_last_status (self,keyword):
    """Get the statuses since the last id and broadcast them"""
        lastid = self.get_lastid(keyword)
        search = api.search (keyword, since_id=lastid)
        if search:
            lastid = search.max_id
            self.lastid[keyword] = lastid
            for s in search:
                if type(s) is Status:
                    tweetstr = s.user.name + " - " + s.text
                    broadcast (tweetstr)

def check_tweets():
    """ Check each keyword for a new tweet"""
    for keyword in keywords:
        lt.get_last_status(keyword)


crontable.append([10, "check_tweets"])


config = yaml.load(open('tweepybot.conf', 'r'))

consumer_key=config['TWEEPY_CONSUMER_KEY']
consumer_secret=config['TWEEPY_CONSUMER_SECRET']
access_token=config['TWEEPY_ACCESS_TOKEN']
access_token_secret=config['TWEEPY_ACCESS_TOKEN_SECRET']
channels = config['CHANNELS']
keywords = config['KEYWORDS']

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
lt = LastTweets(api)


broadcast("Bot started")


if __name__ == '__main__':
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    lt = LastTweets(api)

    while True:
        for keyword in keywords:
            lt.get_last_status(keyword)
        time.sleep (5)
