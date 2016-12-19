import random


def poll_user(word):
    while True:
        letter = input("Enter a letter to guess: ")
        letter = str(letter)
        
        if (len(letter) == 1 or len(letter) == len(word)) & letter.isalpha():
            return letter
        else:
            print("That\'s not a valid letter. Try again")

def pick_word():
	words = ["glorious", "brass", "month", "finger",
	"sky", "whimsical", "top", "certain", "bless",
    "end", "flesh", "crush"]
	
	return random.choice(words)

def game():
    word = pick_word()
    progress = ""
    attempts = 0
    for i in word:
        progress = progress + "_ "

    
    while (progress.find("_") is not -1):
        print(progress)
        
        char = poll_user(word)
        attempts += 1
        char_loc = word.find(char)

        if word == char:
        	progress = ""
        elif progress.find(char) is not -1:
            print("You've already guessed that letter!")
        elif char_loc is -1:
            print("That letter isn't in this word...")
        else:
            while char_loc is not -1:
                prog_loc = char_loc * 2
                progress = progress[:prog_loc] + char + progress[prog_loc + 1:]
                char_loc = word[char_loc + 1:].find(char)

    print("You win! It took you", attempts, "attempts to solve.")
    print("The word was \"" + word + "\"")

def main():
	ans = "GO!"
	while ans.lower() != "q":
		game()
		ans = input("Hit ENTER to player again, hit Q to quit: ")

main()
