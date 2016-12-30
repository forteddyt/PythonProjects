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
location = "base"

########### Definition area of key terms in Definer.py ############

show_dict = {'less' : "_SHORT_", 'more' : "_LONG_", 'stored' : "_STORED_", 'running' : "_RUNNING_"}

###################################################################

# A simple print with a system flush afterwards
def printFlush(string = ''):
	print(string)
	sys.stdout.flush()

def poll_user():
	global location
	given = input(">-" + location + "->")
	given = given.strip()
	given = given.split(" ")
	return given

def definerHelp(function = None, *args):
	if(len(args) > 0):
		printFlush(err)
		return

	if function == None:
		commands = sorted(call_list.keys())
		printFlush("Available commands: ")
		for item in commands:
			printFlush(item + " -> " + call_definitions[item][0])
	else:
		try:
			item = call_definitions[function]
			print(item[0] + "\n" + item[1])
		except KeyError as e:
			print("Function '" + function + "' does not exist")

def close(*arg):
	if(len(args) > 0):
		printFlush(err)
		return

	global location
	global polling
	
	if location == "base":
		printFlush("Closing Definer.py")
		polling = False
	else:
		printFlush("Closing " + location + " editor.")
		location = "base"

def add(*args):
	term = ""

	for item in args:
		term += str(item) + " "
	term = term.strip()

	if(term == ""):
		printFlush(err)
		return

	if(location == "base"):
		if term in running_search_terms.keys():
			printFlush("Search term '" + term + "' already exists")
			return
		else:
			running_search_terms.__setitem__(term, [])
	else:
		if term in running_search_terms.get(location):
			printFlush("Search term '" + term + "' already exists")
			return
		else:
			running_search_terms.get(location).append(term)

	printFlush("Term '" + term + "' added.")


def edit(*args):
	if len(args) == 0:
		printFlush(err)
		return

	tag = None
	if args[0] == "-a" or args[0] == "-r":
		tag = args[0]

	term = ""

	if tag != None and len(args) <= 1:
		printFlush(err)
		return

	global location

	if tag == None:
		for item in args:
			term += str(item) + " "
	else:
		for item in args[1:]:
			term += str(item) + " "
	term = term.strip()

	if tag == "-a":
		add(*args[1:])
		location = term
	elif tag == "-r":
		remove(*args[1:])
	else:
		if location == "base":
			if term in running_search_terms.keys():
				location = term
			else:
				printFlush("Search term '" + term + "' does not exist.")
		else:
			printFlush(err)
			return	


# Sets running search list as stored search list
def store(*args):
	if(len(args) > 0):
		printFlush(err)
		return

	stored_search_terms = running_search_terms.copy()
	printFlush("Running search list stored.")

# Writes stored search list to file
def update(*args):
	if(len(args) > 0):
		printFlush(err)
		return

	base_txt = open(file_path + "base.txt", "r")
	date = base_txt.readline().strip()
	base_txt.close()

	base_txt = open(file_path + "base.txt", "w")
	base_txt.write(date + "\n")
	base_txt.write(str(stored_search_terms) + "\n")
	base_txt.close()

	printFlush("Stored search list written to file.")

# Shorthand for store-ing and update-ing
def save(*args):
	if(len(args) > 0):
		printFlush(err)
		return

	store()
	update()

def show(*args):
	is_short = False
	is_stored = False
	key = None

	if len(args) == 0:
		key = None
	else:
		leading = args[0]
		trailing = args[-1]
		if leading in show_dict.values():
			if leading == trailing and len(args) > 1:
				printFlush(err)
				return

			args = args[1:]
			if leading == show_dict['less']:
				is_short = True
				if len(args) > 0:
					printFlush(err)
					return
			elif leading == show_dict['more']:
				if len(args) > 0:
					printFlush(err)
					return
			elif leading == show_dict['stored']:
				is_stored = True

			if len(args) > 0:
				trailing = args[-1]
				if trailing == show_dict['running'] or trailing == show_dict['stored']:
					printFlush(err)
					return
			else:
				trailing = None
		if trailing in show_dict.values():
			args = args[:-1]
			if trailing == show_dict['less']:
				is_short = True
			elif trailing == show_dict['stored']:
				is_stored = True
				if len(args) > 0:
					printFlush(err)
					return
			elif trailing == show_dict['running']:
				if len(args) > 0:
					printFlush(err)
					return
			
		if len(args) > 0:
			key = ""
			for word in args:
				key += word + " "
			key = key.strip()

	if is_stored:
		cur_list = stored_search_terms
		addon = " in the stored search list."
	else:
		cur_list = running_search_terms
		addon = " in the running search list."

	if key != None:
		if key not in cur_list.keys():
			printFlush("Search topic '" + key + "' does not exist" + addon)
		else:
			printFlush("Search topic '" + key + "'")
			if not is_short:
				printFlush("has terms -> " + str(cur_list.get(key)))
	else:
		for term_key in sorted(cur_list.keys()):
			printFlush("Search topic '" + term_key + "'")
			if not is_short:
				printFlush("has terms -> " + str(cur_list.get(term_key)))
		

call_list = {'close' : close, 'help' : definerHelp, 'show' : show, 'store' : store, 'update' : update, 'save' : save, 'edit' : edit, 'add' : add}
call_definitions = {'close' : ["--close--", "Closes editor if user is editting a <search topic>. Closes Definer otherwise. Does not write any changes in search list to file."],
					'help' : ["--help <function>--", "This function provides a helpful message for functions in Definer. Calling help <function> prints help for Definer object '<function>'. A blank <function> will show available functions"],
					'show' : ["--show [mode1] [<search topic>] [mode2]--", "Shows the given <search topic>'s term list. An optional [mode1] of '" + show_dict['running'] + "'/'" + show_dict['stored'] + "' shows the running/stored <search topic>-pair list. An optional [mode2] of '" + show_dict['less'] + "' will display the <search topic>(s) without the terms. [mode1] defaults to '" + show_dict['running'] + "'.[mode2] defaults to '" + show_dict['more'] + "'. No given <search topic> will display all search_topics."],
					'store' : ["--store--", "Sets the current running search list as the stored search list. Does not 'update' the search list to file."],
					'update' : ["--update--", "Updates the local base.txt file to match the stored search list."],
					'save' : ["--save--", "In short, 'store's then 'update's. Sets the running search list as the stored search list, then updates the local base.txt file to match the stored search list."],
					'edit' : ["--edit [tag] <search topic>--", "Begins editting the existing <search topic>, if exists. Optional [tag] '-a' adds <search topic>, if it does not already exist. Optional [tag] '-r' removes <search topic>, if it exists."],
					'add' : ["--add <search topic/term>--", "Adds the <search topic/term> to the running list, if it does not already exist. Everything after the 'add' command is considered the <search topic/term>'."]}


def formatCallDefinitions():
	char_limit = 35 # Soft max number of characters per line of function definitions

	for key in call_definitions:
		counter = 0
		line = call_definitions.get(key)[1]
		tempLine = ""
		for char in call_definitions.get(key)[1]:
			if counter > char_limit and char == " ":
				temp = line[:counter].strip() + "\n"
				tempLine += temp
				line = line[counter:]
				counter = 0
			counter += 1
		if tempLine == "":
			tempLine = call_definitions.get(key)[1]
		else:
			tempLine += line.strip()

		tempItem = [call_definitions.get(key)[0], tempLine]

		call_definitions.__setitem__(key, tempItem)


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