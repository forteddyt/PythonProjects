# PRAW - https://praw.readthedocs.io/en/latest/index.html
# Script is ran at approximately 11:59 P.M. EST each day

import praw
import datetime

# Obtains a Reddit instance
# client_id and client_secret are reddit user's application's credentials
# user_agent is the general purpose of this script
reddit = praw.Reddit(client_id='1sBmgGrhe_PtkA',
					 client_secret='jeII_nOtB1_xsFNCqd3H-irTc5M',
					 user_agent='/r/WorldNews url+title collector by GETAR_Events_Bot')

# Obtains a Subreddit instance of /r/worldnews
subreddit_worldnews = reddit.subreddit('worldnews')

# Defines a dictionary of search terms to search for. Not case-sensitive
search_terms = {'Saudi Arabia'}

base_txt = open("base.txt", "r")
increment_date = base_txt.readline()
base_txt.close()

start_date = datetime.datetime.strptime(increment_date, "%m/%d/%y")
end_date = start_date + datetime.timedelta(days=6)

cur_date = datetime.datetime.strptime(datetime.date.today().strftime("%m/%d/%y"), "%m/%d/%y")
terminate_date = end_date + datetime.timedelta(days=1)

if cur_date == terminate_date:
	start_date = cur_date

	base_txt = open("base.txt", "w")
	base_txt.write(start_date)
	base_txt.close()

	end_date = start_date + datetime.timedelta(days=6)


str_start_date = str(start_date.month) + "." + str(start_date.day) +"." + str(start_date.year)
str_end_date = str(end_date.month) + "." + str(end_date.day) + "." + str(end_date.year)


timeframe = str_start_date + " - " + str_end_date + ".txt"
weekly_draft = open(timeframe, "a")

# Obtains a Submission instance from a specified Subreddit category
for submission in subreddit_worldnews.top('day', limit = 10):
	weekly_draft.write("--- " + submission.title + " ---\n")
	weekly_draft.write(submission.url + "\n\n")

weekly_draft.close()


# Search /r/worldnews for articles containing a search_terms term
# Only searches for articles created in past 24 hours
for term in search_terms:
	print("Search results for \"" + term + "\"")
	for submission in subreddit_worldnews.search(term, 'relevance', 'cloudsearch', 'day'):
		print('~~~ ' + submission.title + " ~~~")
		print(submission.url)
	print("")

