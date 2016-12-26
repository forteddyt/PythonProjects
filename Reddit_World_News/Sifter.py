
import sys
import os
import time
file_path = os.path.dirname(os.path.realpath(__file__)) + "\\" # Obtains the scripts file path

# A simple print with a system flush afterwards
def printFlush(string = ''):
	print(string)
	sys.stdout.flush()

def renameProcedure():
	import datetime

	printFlush("Obtaining base time...")
	base_txt = open(file_path + "base.txt", "r")
	base_date = datetime.datetime.strptime(base_txt.readline(), "%m/%d/%y")
	base_txt.close()
	printFlush("**Base time obtained.")

	start_date = base_date - datetime.timedelta(days=7)
	end_date = base_date - datetime.timedelta(days=1)

	start_date = start_date.strftime("%m.%d.%y")
	end_date = end_date.strftime("%m.%d.%y")

	global_events_f = file_path + "Global Events - " + str(start_date) + " to " + str(end_date)
	topic_events_f = file_path + "Topic Specific Events - " + str(start_date) + " to " + str(end_date)

	printFlush("Moving the dirt to COPY...")
	try:
		os.rename(global_events_f + ".txt", global_events_f + "COPY.txt")
	except FileExistsError as e:
		printFlush(global_events_f + "COPY.txt already exists, could not create copy.")
#	try:
#		os.rename(topic_events_f + ".txt", topic_events_f + "COPY.txt")
#	except FileExistsError as e:
#		printFlush(topic_events_f + "COPY.txt already axists, couldnot create copy.")
	printFlush("**Dirt moved.")

	printFlush("Creating blank templates...")
	true_txt = open(global_events_f +".txt", "w")
	true_txt.close()
#	true_txt = open(topic_events_f + ".txt", "w")
#	true_txt.close()
	printFlush("**Blank templates created.")


try:
	renameProcedure()
except SystemError as e:
	printFlush("Closing...")
	time.delay(1.5)