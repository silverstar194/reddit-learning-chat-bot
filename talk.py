from reddit import RunBot, Account
import time
import random
import settings
import logging
import logging.handlers
import os

handler = logging.handlers.WatchedFileHandler(
    os.environ.get("LOGFILE", "debug.log"))
formatter = logging.Formatter(logging.BASIC_FORMAT)
handler.setFormatter(formatter)
root = logging.getLogger()
root.setLevel(os.environ.get("LOGLEVEL", "INFO"))
root.addHandler(handler)

if __name__ == '__main__':
	logging.info("Started...")
	while True:
		logging.info("Sleeping")
	# Wait 10 minutes to comment and post because of reddit rate limits
		time.sleep(random.randint(10*60, 100*60))
		# reddit.random_submission()
		account = Account(settings.REDDIT_CLIENT_ID,settings.REDDIT_SECRET,settings.REDDIT_PASSWORD,settings.REDDIT_USER_AGENT,settings.REDDIT_USERNAME,0)
		bot = RunBot(account)
		bot.random_reply()
        
        
