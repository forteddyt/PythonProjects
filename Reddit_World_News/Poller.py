# PRAW - https://praw.readthedocs.io/en/latest/index.html
# Script is ran at approximately 11:59 P.M. EST each day
# Formatting into a .docx is done elsewhere

import sys

# A simple print with a system flush afterwards
def printFlush(string = ''):
	print(string)
	sys.stdout.flush()

# Ensures the PRAW package is installed
def checkImports():
	try:
		import praw
	except ImportError as e:
		# Asks user to install PRAW if they do not have it
		printFlush("The Python Reddit API Wrapper (PRAW) package is not currently installed on this machine."
				+ "\n The PRAW package is needed in order for this script to run.")
		resp = input("Would you like to install the PRAW package?\n\t[Y]es or [N]o:")
		
		# If invalid reponse is given, continuing asking until a valid response is given
		while (resp.upper() != "Y" and resp.upper() != "YES"
			and resp.upper() != "N" and resp.upper() != "NO"):
			resp = input("Invalid response.\nWould you like to install the PRAW package?\n\t[Y]es or [N]o: ")
		
		# Install PRAW with pip if the user allows it, exit the script otherwise
		if (resp.upper() == "Y" or resp.upper() == "YES"):
			printFlush("Installing PRAW...")
			import pip
			pip.main(['install', 'praw'])
			printFlush("**PRAW installed.")
		else:
			import time
			printFlush("Unable to run script without appropriate packages.\nExiting...")
			time.sleep(1)
			sys.exit(0)

def pollReddit():
	checkImports()
	import datetime
	import os
	import praw

	file_path = os.path.dirname(os.path.realpath(__file__)) + "\\" # Obtains the scripts file path
	max_num_posts = 10 # Max amount of posts to collect per day
	search_terms = {"Saudi", "Arabia"} # Defines a dictionary of search terms to search for. Not case-sensitive
	
	printFlush("Starting script...")

	# Obtains a Reddit instance
	# client_id and client_secret are reddit user's application's credentials
	# user_agent is the general purpose of this script
	reddit = praw.Reddit(client_id='1sBmgGrhe_PtkA',
						 client_secret='jeII_nOtB1_xsFNCqd3H-irTc5M',
						 user_agent='/r/WorldNews url+title collector by GETAR_Events_Bot')

	# Obtains a Subreddit instance of /r/worldnews
	subreddit_worldnews = reddit.subreddit('worldnews')
	
	printFlush("Obtaining base information...")

	# Used to determine the starting point of weekly polling intervals
	# ie. If date in base.txt is 12/20/16 the intervals would start from the 20th
	try:
		base_txt = open(file_path + "base.txt", "r")
	except Exception as e:
		printFlush("No base.txt found, creating...")
		base_txt = open(file_path + "base.txt", "w")
		base_txt.close()
		base_txt = open(file_path + "base.txt", "r")
		printFlush("**base.txt created.")
	increment_date = base_txt.readline()
	base_txt.close()

	# Stores current date as MM/DD/YY
	cur_date = datetime.datetime.strptime(datetime.date.today().strftime("%m/%d/%y"), "%m/%d/%y")

	# Determines if there is data in the base.txt file
	# Writes to file and sets current date (DD/MM/YY format) as increment_date 
	if increment_date == "":
		printFlush("No initial date found, setting '" + cur_date.strftime('%x') + "' as initial date...")
		increment_date = str(cur_date.strftime('%x'))
		base_txt = open(file_path + "base.txt", "a")
		base_txt.write(cur_date.strftime('%x'))
		base_txt.close()
		printFlush("**Initial date is now set.")

	printFlush("**Base information obtained.")

	# Creates a start_date and end_date based off base.txt file
	start_date = datetime.datetime.strptime(increment_date, "%m/%d/%y")
	end_date = start_date + datetime.timedelta(days=6)

	# Terminal date is a day after the end date
	terminate_date = end_date + datetime.timedelta(days=1)

	printFlush("Checking new date cycle...")

	# Determines if the next interval cycle is to begin
	# Overwrites base.txt with appropriate date
	if cur_date == terminate_date:
		start_date = cur_date

		printFlush("Creating new cycle...")

		base_txt = open(file_path + "base.txt", "w")
		base_txt.write(start_date)
		base_txt.close()

		printFlush("**New cycle create.")

		end_date = start_date + datetime.timedelta(days=6)
	else:
		printFlush("**No new cycle needed.")


	# Creates a string representation of the dates in MM.DD.YY format
	str_start_date = str(start_date.month) + "." + str(start_date.day) +"." + str(start_date.year)
	str_end_date = str(end_date.month) + "." + str(end_date.day) + "." + str(end_date.year)

	# Creates a string from the start to the end date
	timeframe = str_start_date + " to " + str_end_date

	printFlush("Starting general searches...")

	# Creates and opens a weekly .txt file 
	weekly_title = "Global Events - " + timeframe + ".txt"
	weekly_draft = open(file_path + weekly_title, "a")

	index = 1

	# Obtains a Submission instance from a specified Subreddit category
	for submission in subreddit_worldnews.top('day', limit = max_num_posts):
		weekly_draft.write(submission.id + "\n")
		weekly_draft.write(submission.title + "\n")
		weekly_draft.write(submission.url + "\n\n\n")
		printFlush(str(index) + " written to file...")
		index += 1

	weekly_draft.close()

	printFlush("**General searches complete.")
	printFlush("Starting topic-specific searches...")

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
			topic_draft.write(submission.id + "\n")
			topic_draft.write(submission.title + "\n")
			topic_draft.write(submission.url + "\n\n\n")
			printFlush("Topic " + str(topic_index) + ", index " + str(index) + " writtin to file...")
			index += 1
		topic_index += 1
		index = 1

	topic_draft.close()
	printFlush("**Topic-specific searches complete.")

	printFlush("**Script complete.")

try:
	pollReddit()
except SystemExit as e:
	printFlush("**EXITING SCRIPT**")