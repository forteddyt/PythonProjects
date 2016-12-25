# PRAW - https://praw.readthedocs.io/en/latest/index.html
# Script is ran at approximately 11:59 P.M. EST each day
# Formatting into a .docx is done elsewhere

import praw
import datetime
import os

# Obtains the scripts file path
file_path = os.path.dirname(os.path.realpath(__file__)) + "\\"

# Max amount of posts to collect per day
num_posts = 10

print("Starting script...")

# Obtains a Reddit instance
# client_id and client_secret are reddit user's application's credentials
# user_agent is the general purpose of this script
reddit = praw.Reddit(client_id='1sBmgGrhe_PtkA',
					 client_secret='jeII_nOtB1_xsFNCqd3H-irTc5M',
					 user_agent='/r/WorldNews url+title collector by GETAR_Events_Bot')

# Obtains a Subreddit instance of /r/worldnews
subreddit_worldnews = reddit.subreddit('worldnews')

# Defines a dictionary of search terms to search for. Not case-sensitive
search_terms = {"Saudi Arabia"}

print("Obtaining base information...")

# Used to determine the starting point of weekly polling intervals
# ie. If date in base.txt is 12/20/16 the intervals would start from the 20th
base_txt = open(file_path + "base.txt", "r")
increment_date = base_txt.readline()
base_txt.close()

print("**Base information obtained.")

# Creates a start_date and end_date based off base.txt file
start_date = datetime.datetime.strptime(increment_date, "%m/%d/%y")
end_date = start_date + datetime.timedelta(days=6)

# Terminal date is a day after the end date
cur_date = datetime.datetime.strptime(datetime.date.today().strftime("%m/%d/%y"), "%m/%d/%y")
terminate_date = end_date + datetime.timedelta(days=1)

print("Checking new date cycle...")

# Determines if the next interval cycle is to begin
# Overwrites base.txt with appropriate date
if cur_date == terminate_date:
	start_date = cur_date

	print("Creating new cycle...")

	base_txt = open(file_path + "base.txt", "w")
	base_txt.write(start_date)
	base_txt.close()

	print("**New cycle create.")

	end_date = start_date + datetime.timedelta(days=6)
else:
	print("**No new cycle needed.")


# Creates a string representation of the dates in MM.DD.YY format
str_start_date = str(start_date.month) + "." + str(start_date.day) +"." + str(start_date.year)
str_end_date = str(end_date.month) + "." + str(end_date.day) + "." + str(end_date.year)

# Creates a string from the start to the end date
timeframe = str_start_date + " to " + str_end_date

print("Starting general searches...")

# Creates and opens a weekly .txt file 
weekly_title = "Global Events - " + timeframe + ".txt"
weekly_draft = open(file_path + weekly_title, "a")

index = 1

# Obtains a Submission instance from a specified Subreddit category
for submission in subreddit_worldnews.top('day', limit = num_posts):
	weekly_draft.write(submission.title + "\n")
	weekly_draft.write(submission.url + "\n\n")
	print(str(index) + " written to file...")
	index += 1

weekly_draft.close()

print("**General searches complete.")
print("Starting topic-specific searches...")

index = 1
topic_index = 1

# Creates and opens a weekly, topic-specific .txt file
# Topic-specific refers to the topics in the search_terms dictionary
topic_title = "Topic Specific Events - " + timeframe + ".txt"
topic_draft = open(file_path + topic_title, "a")

# Search /r/worldnews for articles containing a search_terms term
# Only searches for articles created in past 24 hours
for term in search_terms:
	topic_draft.write("Search results for \"" + term + "\" - " + str(cur_date) + "\n")
	for submission in subreddit_worldnews.search(term, 'relevance', 'cloudsearch', 'day'):
		topic_draft.write(submission.title + "\n")
		topic_draft.write(submission.url + "\n\n")
		print("Topic " + str(topic_index) + ", index " + str(index) + " writtin to file...")
		index += 1
	topic_index += 1
	index = 1

topic_draft.close()
print("**Topic-specific searches complete.")


print("**Script complete.")