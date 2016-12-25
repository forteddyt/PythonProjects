# PRAW - https://praw.readthedocs.io/en/latest/index.html
import praw

# Obtains a Reddit instance
# client_id and client_secret are reddit user's application's credentials
# user_agent is the general purpose of this script
reddit = praw.Reddit(client_id='1sBmgGrhe_PtkA',
					 client_secret='jeII_nOtB1_xsFNCqd3H-irTc5M',
					 user_agent='/r/WorldNews url+title scraper by GETAR_Events_Bot')


# Obtains a Subreddit instance of /r/worldnews
subreddit_worldnews = reddit.subreddit('worldnews')

# Defines a dictionary of search terms to search for. Not case-sensitive
search_terms = {'Saudi Arabia', 'school'}


# Obtains a Submission instance from a specified Subreddit category
for submission in subreddit_worldnews.top('day', limit = 10):
	print('--- ' + submission.title + ' ---')
	print(submission.url)

print('--')

for term in search_terms:
	print("Search results for \"" + term + "\"")
	for submission in subreddit_worldnews.search(term, 'relevance', 'cloudsearch', 'day'):
		print('~~~ ' + submission.title + " ~~~")
		print(submission.url)
	print("")
