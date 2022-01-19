import random
import json

# first we need to get the data from the json file.
# choose a random word, make sure it has no spaces.

# start the game

# user will input a letter at a time.
# the input should be checked against the word.
# if exists, it should populate the word template.
# if not, add to "used words" list. we will use a 'set' since it is not allowing dups.

# we show the user the words he already used.

# user will have a limited amount of guesses.
# if succeeded, show messsage. If # of guesses is down to 0, show lost message.

###************************************************************************************************###

# get list of words from file
import string

with open('data.json', 'r') as file:
    words_list = json.load(file)['data']


def get_word(words):
    word = random.choice(words_list)

    while '-' in word or ' ' in word:
        word = random.choice(words_list)

    return word.upper()


def hangman():
    word = get_word(words_list)
    alphabet = set(string.ascii_uppercase)
    word_letters = set(word)
    used_letters = set()

    lives = 6

    while len(word_letters) > 0 and lives > 0:  # this will make sure we keep getting user input.

        #show the used letters
        print("You have ", lives,"lives left. You have used these letters: ", " ".join(used_letters))

        #the current word state.
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1
                print("\nThe letter is not in the word.\n")

        elif user_letter in used_letters:
            print("You have already used that character")

        else:
            print("Invalid character. Please try again.")

    if lives == 0:
        print("GAME OVER! You lost. The word is:", word)
    else:
        print("You guessed the word", word, "!")

print(hangman())
