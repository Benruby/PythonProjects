import random


# let the user guess a number
def guess(x):
    random_number = random.randint(1, x)

    guess = 0

    while guess != random_number:

        guess = int(input(f"Please guess a number from 1 to {x}: "))

        if guess < random_number:
            print("The number you guessed is too LOW.")
        elif guess > random_number:
            print("The number you guessed is too HIGH.")

    print("You guessed the number correctly!")


# let the computer guess my secret number
def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':

        if low != high:

            guess = random.randint(low, high) #throws an error if low=high


        else:

            guess = low

        feedback = input(f"Is {guess} is to low (L), too high (H) or correct (C)?").lower()

        if feedback == 'l':
            low = guess + 1
        elif feedback == 'h':
            high = guess - 1
    print(f"The computer guess the number {guess} correctly!")


computer_guess(1000)
