Twitter bot for Slack
=====================

The idea is to integrate some twitter functionalities into a Slack bot.
For now, it just grabs the last tweets for a particular keyword and
broadcast it into different channels.

You need to get 

# Quick Start

1. Download the python-rtmbot code

        git clone git@github.com:slackhq/python-rtmbot.git
        cd python-rtmbot

2. Install dependencies ([virtualenv](http://virtualenv.readthedocs.org/en/latest/) is recommended.)

        pip install -r requirements.txt
        pip install tweepy

3. Configure rtmbot (https://api.slack.com/bot-users)

        cp doc/example-config/rtmbot.conf .
        vi rtmbot.conf
          SLACK_TOKEN: "xoxb-11111111111-222222222222222"

4. Download and enable this plugin

        git submodule add -f git://github.com/juli1/tweepybot.git plugins/tweepy

5. Create a configuration file for tweepy that indicates the slack channels and the hashtag you follow 
   The file must be in the root directory of the rtmbot and have the twitter API access keys.

        cp -f plugins/tweepy/tweepybot.conf .

   and edit the tweepybot.conf file

6. Start

        ./rtmbot.py
