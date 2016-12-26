# Sifter.py should be in the same directory as Poller.py
# Sifter is run the day after the week-long Poller interval ends
# ie. If Poller polls from 12/10/16 to 12/16/16, Sifter is run on 12/17/16

import sys
import os
import time
file_path = os.path.dirname(os.path.realpath(__file__)) + "\\" # Obtains the scripts file path

# A simple print with a system flush afterwards
def printFlush(string = ''):
	print(string)
	sys.stdout.flush()

# Renames the Global Events and Topic Specific Events files to end with COPY.txt
# Recreates the Global Events and Topic Specific Events files as blank .txt with original names
def renameProcedure():
	import datetime

	# Uses base.txt to determine the polling interval
	printFlush("Obtaining base time...")
	base_txt = open(file_path + "base.txt", "r")
	base_date = datetime.datetime.strptime(base_txt.readline(), "%m/%d/%y")
	base_txt.close()
	printFlush("**Base time obtained.")

	# Since Sifter is run the day after a polling interval is complete, 
	# the file that will be sifted spans from a week ago to yesterday
	start_date = base_date - datetime.timedelta(days=7)
	end_date = base_date - datetime.timedelta(days=1)

	start_date = start_date.strftime("%m.%d.%y")
	end_date = end_date.strftime("%m.%d.%y")

	# Naming convention from Poller used in storing file locations
	# Poller.py stores with RAW tag. RAW tag added temporarily in upcoming code
	global_events_f = file_path + "Global Events - " + str(start_date) + " to " + str(end_date)
	topic_events_f = file_path + "Topic Specific Events - " + str(start_date) + " to " + str(end_date)

	# Attempts to rename the dity Global Events .txt to end with COPY
	printFlush("Moving the dirt to COPY...")
	try:
		os.rename(global_events_f + "RAW.txt", global_events_f + "COPY.txt")
	except FileExistsError as e:
		printFlush(global_events_f + "COPY.txt already exists, could not create copy.")

	# Attempts to rename the dity Topic Specific Events .txt to end with COPY	
	try:
		os.rename(topic_events_f + "RAW.txt", topic_events_f + "COPY.txt")
	except FileExistsError as e:
		printFlush(topic_events_f + "COPY.txt already axists, couldnot create copy.")
	printFlush("**Dirt moved.")

	# Then creates new, blank .txt files with the original names
	# These blank .txt will be filled with only unique posts
	printFlush("Creating empty templates...")
	true_txt = open(global_events_f +".txt", "w")
	true_txt.close()
	true_txt = open(topic_events_f + ".txt", "w")
	true_txt.close()
	printFlush("**Empty templates created.")

	name_set = [global_events_f, topic_events_f]
	return name_set

# 'Pan's the Global Events file
# Only copys over unique posts from the COPY file to the orginal file
# global_name is the file path to the original Global Events file
def panGlobal(global_name):
	id_list_len = 0
	id_set = set([])
	dirt = open(global_name + "COPY.txt", "r")
	dish = open(global_name + ".txt", "a")

	counter = 0
	add_post = False

	printFlush("Panning the 'Global' dirt into the 'Global' dish...")
	for line in dirt.readlines():
		# File formatting conventions from Poller.py dictates a new post begins every 4 lines
		if counter % 4 == 0:
			add_post = False
			id_set.add(line)
			printFlush("Sifting post #" + str(int(counter / 4) + 1) + "...")

		# If adding the ID of this post to the set increases it's length, it must be a unique post
		if (counter % 4 == 0 and id_list_len != len(id_set)):
			id_list_len += 1
			add_post = True

		# Writes the next 4 lines into the original files
		if (add_post == True and counter % 4 != 0):
			dish.write(line)

		counter += 1
	printFlush("**Panning complete. 'Global' dish filled with gold!")

	dirt.close()
	dish.close()

# 'Pan's the Specific Events file
# Only copys over unique posts from the COPY file to the orginal file
# specific_name is the file path to the original Specific Events file
def panSpecific(specific_name):
	pass
#	 NEED TO IMPLEMENT THE TOPIC SPECIFIC EVENTS PANNING!


# Deletes both the Global Events COPY and Topic Specific Events COPY files
# global_name and specific_name are the file paths to the original files
def dump(global_name, specific_name):
	printFlush("Dumping 'Global' COPY...")
	os.remove(global_name + "COPY.txt")
	printFlush("**'Global' COPY dumped.")

	printFlush("Dumping specific COPY...")
	os.remove(specific_name + "COPY.txt")
	printFlush("**Specific COPY dumped.")

try:
	printFlush("Starting Sifter.py script...")

#	name_set = renameProcedure()
#	panGlobal(name_set[0])
#	panSpecific(name_set[1])
#	dump(name_set[0], name_set[1])

	printFlush("**Script complete.")

	time.sleep(1.5)

	temp = {'Arabia' : [1, 2, 3], 'Saudi' : [1, 3, 4]}
	print(temp['Arabia'])
	print(temp['School Shooting'])
	

except SystemError as e:
	printFlush("**EXITING SCRIPT**")
	time.delay(1.5)
