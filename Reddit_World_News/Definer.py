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
	given = input(">>")
	given = given.strip()
	given = given.split(" ")
	return given

def definerHelp(function = None, *args):
	if function == None:
		commands = call_list.keys()
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

call_list = {'close' : close,'help' : definerHelp}
call_definitions = {'close' : "Closes Definer without saving search list progress.",
					'help' : "This function provides a helpful message for functions in Definer. Calling help <function> prints help for Definer object '<function>'."}
def formatCallDefinitions():
	char_limit = 35 # Soft max number of characters per line of function definitions

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