import random

def generate_num(upper_bound = 100):
    return random.randint(1, upper_bound)

def guess_num(ans):
    print("Guess the number!\n")
    is_correct = False
    while is_correct == False:
        guess = input("Enter your guess: ")
        try:
            guess = int(guess)
        except ValueError:
            print("That's not an int!")
            continue
        if guess < ans:
            print("That's too low!")
        elif guess > ans:
            print("That's too high!")
        else:
            print("You got it!")
            is_correct = True

def main():
    num = generate_num()
    guess_num(num)

main()
