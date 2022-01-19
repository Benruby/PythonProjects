import random

#player against computer.
#define rules: r>s, s>p , p>r

def play():
    # get user input
    user = input("'r' for rock, 'p' for paper, 's' for scissors: ")

    # get computer input
    computer = random.choice(["r", "p", "s"])

    # what if inputs are identical.
    if user == computer:
        return 'tie!'

    # check for wins, user as winning player.
    if check_win(user, computer):
        return "You win!"

    return "you lose!"

# this function check all the posibilities of a win. no need to check also for loses. DRY
#the winner is always player1 passed to the function.
def check_win(player1, player2):
    if (player1 == 'r' and player2 == 's') or (player1 == 's' and player2 == 'p') or (player1 == 'p' and player2 == 'r'):
        return True

print(play())
