def direction_to_number(char):
	switch = {
		"N": 1,
		"E": 2,
		"S": 3,
		"W": 4,
	}

	return switch.get(char, "invalid");

def build_area():
	area = {}

	area["Entrance Way"] = [0, "Kitchen", "Living Room", None, None]
	area["Living Room"] = [0, "Dining Room", None, None, "Entrance Way"]
	area["Kitchen"] = [0,  None, "Dining Room", "Entrance Way", "Hallway"]
	area["Dining Room"] = [0, None, None, "Living Room", "Kitchen"]
	area["Hallway"] = [0, None, "Kitchen", None, "Family Room"]
	area["Family Room"] = [0, None, "Hallway", None, None]

	return area



def main():
	has_basket = False
	has_eggs = False
	has_delivered = False
	has_escaped = False

	def dialogue(room):
		nonlocal has_basket, has_eggs, has_delivered, has_escaped

		if room == "Entrance Way" and not has_delivered:
			print("You can exit through here after delivering the eggs to Cooper...")
		elif room == "Entrance Way" and has_delivered:
			has_escaped = True
			print("With the eggs devlivered, you make your escape!")
		elif room == "Living Room":
			print("What a comfortable looking room! Too bad there's nothing else interesting about it...")
		elif room == "Kitchen" and not has_eggs:
			has_eggs = True
			print("You found the eggs!")
			if has_basket:
				print("Now that you have the basket and the eggs, you can deliver them to Cooper!")
			else:
				print("Now you have to find the basket...")
		elif room == "Kitchen" and has_eggs:
			print("Flour, milk, and sugar. If you hadn't taken those eggs, Cooper could've baked a cake...")
		elif room == "Dining Room" and not has_basket:
			has_basket = True
			print("You found the basket!")
			if has_eggs:
				print("Now that you have the basket and eggs, you can deliver them to Cooper!")
			else:
				print("Now you have to find the eggs...")
		elif room == "Dining Room" and has_basket:
			print("The Dining Room table is littered with items you removed from the basket when you took it...")
		elif room == "Hallway":
			print("It's a coordior that leads to somewhere...")
		elif room == "Family Room" and has_basket and has_eggs:
			has_delivered = True
			print("You find a sleeping Cooper and deliver the basket full of eggs. Now quickly, make your escape!")
		elif room == "Family Room" and (not has_basket or not has_eggs):
			print("Cooper's sound asleep. Better not wake him up.")
			if not has_basket:
				print("You still need to find the basket, better keep looking!")
			elif not has_eggs:
				print("You still need to find the eggs, better keep looking!")
			else:
				print("You haven't found either of the items! That's literally impossible!")



	area = build_area()

	print("Hello, Ben! You have been tasked with an important assignment:")
	print("You're going to need to find eggs, find and fill a basket with eggs, deliver it to Cooper, and then make your escape!")
	ans = input("Are you ready? Y/N : ")

	while ans.lower() != "y":
		ans = input("I see... How about now? Are you ready? Y/N: ")

	cur_loc = "Entrance Way"

	while not has_escaped:
		room = area[cur_loc]
		if room[0] > 0:
			print("\nYou are back at the", cur_loc + ".")
		else:
			print("\nYou enter the", cur_loc + ".")
		room[0] += 1

		dialogue(cur_loc)
		if has_escaped:
			continue

		next_loc = None

		while next_loc == None:
			path = input("Which way do you go? North, East, South, or West? N/E/S/W: \n")
			pos = direction_to_number(path)
			while pos is "invalid":
				print("That's not a valid direction.")
				path = input("Which way do you go? North, East, South, or West? N/E/S/W: \n")
				pos = direction_to_number(path)

			next_loc = room[pos]

			if next_loc == None:
				print("\nYou hit a wall. You are still in the " + cur_loc + ".")

		cur_loc = next_loc

	print("\nCongrats! You've succesfully completed the mission!")

main()