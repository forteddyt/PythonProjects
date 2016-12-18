import random

def roll(sides=6):
    return random.randint(1, sides)

def dice_roll(poll_input = True):
    num_sides = 6
    rolling = True
    while rolling:
        if poll_input:
            response = input("Roll the die? Y for YES, N for NO: ")
            if(response.lower() == "y"):
                print("You rolled a ", roll(num_sides))
            else:
                rolling = False
        else:
            return roll(num_sides)
    print("Thanks for playing.")

def average_rolls():
    print("Calculating the average dice roll values...")
    
    r1 = 0
    r2 = 0
    r3 = 0
    r4 = 0
    r5 = 0
    r6 = 0

    count = 0
    rand_value = random.randint(500,5000)
    while count < rand_value:
        count = count + 1
        rolled_value = dice_roll(False)
        if rolled_value == 1:
            r1 = r1 + 1
        elif rolled_value == 2:
            r2 = r2 + 1
        elif rolled_value == 3:
            r3 = r3 + 1
        elif rolled_value == 4:
            r4 = r4 + 1
        elif rolled_value == 5:
            r5 = r5 + 1
        else:
            r6 = r6 + 1
    
    print("Roll average of each value:\n")
    print("1 = ", r1/rand_value * 100)
    print("2 = ", r2/rand_value * 100)
    print("3 = ", r3/rand_value * 100)
    print("4 = ", r4/rand_value * 100)
    print("5 = ", r5/rand_value * 100)
    print("6 = ", r6/rand_value * 100)

def main():
    average_rolls()
    
main()
