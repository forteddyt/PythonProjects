# Definer.py should be in the same directory as Poller.py
# Definer should only be run manually
# Definer is used to define what search_topics and their search terms
# Definer edits the base.txt file, line 2

import os
import sys
from Poller import getSearchTerms
file_path = os.path.dirname(os.path.realpath(__file__)) + "\\" # Obtains the scripts file path
stored_search_terms = getSearchTerms()
running_search_terms = stored_search_terms.copy()
err = "Invalid combination"
polling = True

########### Definition area of key terms in Definer.py ############

show_dict = {'less' : "_SHORT_", 'more' : "_LONG_", 'stored' : "_STORED_", 'running' : "_RUNNING_"}

###################################################################

# A simple print with a system flush afterwards
def printFlush(string = ''):
	print(string)
	sys.stdout.flush()

def poll_user():
	given = input(">>")
	given = given.strip()
	given = given.split(" ")
	return given

def definerHelp(function = None, *args):
	if function == None:
		commands = sorted(call_list.keys())
		printFlush("Available commands: ")
		for item in commands:
			printFlush(item)
	else:
		try:
			print(call_definitions[function])
		except KeyError as e:
			print("Function '" + function + "' does not exist")

def close(*arg):
	printFlush("Closing Definer.py")
	global polling
	polling = False

def show(*args):
	is_short = False
	is_stored = False

	if len(args) == 0:
		key = None
	else:
		leading = args[0]
		trailing = args[-1]
		if leading == trailing and leading in show_dict.values():
			if len(args) > 1:
				printFlush(err)
				return
			else:
				key = None
				if leading == show_dict['stored']:
					is_stored = True
				elif leading == show_dict['less']:
					is_short = True
		elif leading in show_dict.values():
			if leading == show_dict['less'] or leading == show_dict['more']:
				printFlush(err)
				return
			elif leading == show_dict['stored']:
				is_stored = True
			
			if trailing not in show_dict.values():
				key = args[1:]
			else:
				key = args[1:-1]
				if trailing == show_dict['stored'] or trailing == show_dict['running']:
					printFlush(err)
					return
				elif trailing == show_dict['less']:
					is_short = True

	if is_stored:
		cur_list = stored_search_terms
	else:
		cur_list = running_search_terms


	if key != None:
		printFlush("Search topic '" + key + "'")
		if not is_short:
			printFlush("has terms -> " + str(cur_list.get(key)))
	else:
		for term_key in sorted(cur_list.keys()):
			printFlush("Search topic '" + term_key + "'")
			if not is_short:
				printFlush("has terms -> " + str(cur_list.get(term_key)))
		

call_list = {'close' : close, 'help' : definerHelp, 'show': show}
call_definitions = {'close' : "--close-- Closes Definer without setting the running list as the stored list.",
					'help' : "--help <function>-- This function provides a helpful message for functions in Definer. Calling help <function> prints help for Definer object '<function>'. A blank <function> will show available functions",
					'show' : "--show [mode1] [<search topic>] [mode2]-- Shows the given <search topic>'s term list. An optional [mode1] of '" + show_dict['running'] + "' shows the running <search topic>-term pair list while an optional [mode1] of '" + show_dict['stored'] + "' shows the stored <search topic>-pair list. An optional [mode2] of '" + show_dict['less'] + "' will display the <search topic>(s) without the terms. [mode1] defaults to '" + show_dict['running'] + "'.[mode2] defaults to '" + show_dict['more'] + "'. No given <search topic> will display all search_topics."}
def formatCallDefinitions():
	char_limit = 25 # Soft max number of characters per line of function definitions

	for key in call_definitions:
		counter = 0
		line = call_definitions.get(key)
		tempLine = ""
		for char in call_definitions.get(key):
			if counter > char_limit and char == " ":
				temp = line[:counter].strip() + "\n"
				tempLine += temp
				line = line[counter:]
				counter = 0
			counter += 1
		if tempLine == "":
			tempLine = call_definitions.get(key)
		else:
			tempLine += line.strip()
		call_definitions.__setitem__(key, tempLine)


formatCallDefinitions()
while polling == True:
	try:
		item = poll_user()
		command = item[0]
		args = item[1:]
		call_list.get(command)(*args)
	except TypeError as e:
		print(e)
		printFlush(command + " command not found")