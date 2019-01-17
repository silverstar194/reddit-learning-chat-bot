from reddit import RunBot, Account
import time
import random
import settings

if __name__ == '__main__':
    while True:
       # reddit.random_submission()
       	account = Account(settings.REDDIT_CLIENT_ID,settings.REDDIT_SECRET,settings.REDDIT_PASSWORD,settings.REDDIT_USER_AGENT,settings.REDDIT_USERNAME,0)
        bot = RunBot(account)
        bot.random_reply()
        # Wait 10 minutes to comment and post because of reddit rate limits
        time.sleep(15)
