import praw
import time
import random
import bot
import logging

class Account:
    def __init__(self, REDDIT_CLIENT_ID, REDDIT_SECRET, REDDIT_PASSWORD, REDDIT_USER_AGENT, REDDIT_USERNAME, timezone):
        self.REDDIT_CLIENT_ID = REDDIT_CLIENT_ID
        self.REDDIT_SECRET = REDDIT_SECRET
        self.REDDIT_PASSWORD = REDDIT_PASSWORD
        self.REDDIT_USER_AGENT = REDDIT_USER_AGENT
        self.REDDIT_USERNAME = REDDIT_USERNAME
        self.timezone = timezone


class RunBot:
    
    def __init__(self, account):
        self.api = praw.Reddit(client_id=account.REDDIT_CLIENT_ID,
                         client_secret=account.REDDIT_SECRET,
                         password=account.REDDIT_PASSWORD,
                         user_agent=account.REDDIT_USER_AGENT,
                         username=account.REDDIT_USERNAME)
        self.account = account

    def random_submission(self):
        # Get a random submission from a random subreddit
        random_submission = api.subreddit('all').random()

        # Check if there's any items in the submissions list. If not display error
        if random_submission:

            try:
                # Check if the we're reposting a selfpost or a link post.
                # Set the required params accodingly, and reuse the content
                # from the old post
                if random_submission.is_self:
                    params = {"title":random_submission.title, "selftext":random_submission.selftext}
                else:
                    params = {"title":random_submission.title, "url":random_submission.url}

                # Submit the same content to the same subreddit. Prepare your salt picks
                self.api.subreddit(random_submission.subreddit.display_name).submit(**params)
            except Exception as e:
                print e

        else:
            print 'something broke'


    def random_reply(self):
        # Choose a random submission from /r/all that is currently hot
        submission = random.choice(list(self.api.subreddit('all').hot()))
        # Replace the "MoreReplies" with all of the submission replies
        submission.comments.replace_more(limit=0)

        # Choose a random top level comment
        comment = random.choice(submission.comments.list())

        try:
            # Pass the users comment to chatbrain asking for a reply
            response = bot.brain.reply(comment.body)
            if len(response) < 80:
                logging.info("http://www.reddit.com"+comment.permalink)
                logging.info("Comment: " +comment.body)
                logging.info("Bot: "+response)
                logging.info("#"*80+"\n\n")
                try:
                    # Reply tp the same users comment with chatbrains reply
                    reply = comment.reply(response)
                except Exception as e:
                     logging.info("reply FAILED")
                     logging.info(e)

            else:
                 logging.info("Too long"+len(response))
       
        except Exception as e:
            logging.info(e)

        

