import praw
import time
import config
import os

def bot_login():
	reddit = praw.Reddit(client_id = '',
                             client_secret = '',
                             user_agent = '',
                             username = '',
			     password = '')

	return reddit

def run_bot(reddit, comments_replied_to):
	print ("Searching last 100 comments")

	for comment in reddit.subreddit('').comments(limit=100):
		if "" in comment.body and comment.id not in comments_replied_to and comment.author != reddit.user.me():
			print ("String with '' found in comment ") + comment.id
			comment.reply("")
			print ("Replied to comment ") + comment.id

			comments_replied_to.append(comment.id)

			with open ("comments_replied_to.txt", "a") as f:
				f.write(comment.id + "\n")

	print ("Search Finished")

	print (comments_replied_to)

	print ("Sleeping")		
	time.sleep(10)

def get_saved_comments():
	if not os.path.isfile("comments_replied_to.txt"):
		comments_replied_to = []
	else:
		with open("comments_replied_to.txt", "r") as f:
			comments_replied_to = f.read()
			comments_replied_to = comments_replied_to.split("\n")
			comments_replied_to = filter(None, comments_replied_to)

	return comments_replied_to

reddit = bot_login()
comments_replied_to = get_saved_comments()
print (comments_replied_to)

while True:
	run_bot(reddit, comments_replied_to)
