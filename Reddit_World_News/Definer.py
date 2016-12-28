# Definer.py should be in the same directory as Poller.py
# Definer should only be run manually
# Definer is used to define what search_topics and their search terms
# Definer edits the base.txt file, line 2

import os
import sys
file_path = os.path.dirname(os.path.realpath(__file__)) + "\\" # Obtains the scripts file path
polling = True

# A simple print with a system flush afterwards
def printFlush(string = ''):
	print(string)
	sys.stdout.flush()

def poll_user():
	return input(">>")

def definerHelp():
	pass

def close():
	printFlush("Closing Definer.py")
	global polling
	polling = False

call_list = {'close' : close,'help' : definerHelp}
while polling == True:
	try:
		command = poll_user()
		call_list.get(command)()
	except TypeError as e:
		printFlush(command + " command not found")
