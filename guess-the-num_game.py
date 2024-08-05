import random

print("Welcome to the Guess the Number game.")
print("You and your friend(s) have to guess a number that the computer chooses.")
print("The one who guesses the number in the fewest attempts will be the winner.")

def valip2():
    while True:
        user_input = input("Enter the number (1-1000): ")
        if user_input.isdigit() and 1 <= int(user_input) <= 1000:
            return int(user_input)
        else:
            print("Invalid input. Please enter a number between 1 and 1000.")

def runGame():
    a = input("Enter the names of members separated by commas (e.g., Alice,Bob): ")
    members = [name.strip() for name in a.split(",")]
    lm = len(members)
    print("The game is starting...")
    attempts = []

    for i in range(lm):
        print(f"{members[i]}, it's your turn.")
        num = random.randint(0, 1000)
        att = 0
        while True:
            guess = valip2()
            att += 1
            if guess > num:
                print("Too high, try again!")
            elif guess < num:
                print("Too low, try again!")
            else:
                print(f"{members[i]}, you've guessed the number in {att} attempts!")
                break
        attempts.append(att)
        print("----------------------------------------")

    print("Final attempts:")
    for j in range(lm):
        print(f"{members[j]}: {attempts[j]} attempts")

    min_attempts = min(attempts)
    winners = [i for i, x in enumerate(attempts) if x == min_attempts]

    if len(winners) == 1:
        winner = winners[0]
        print(f"And the winner is {members[winner]}, who guessed the number in {min_attempts} attempts!")
        print(f"Congratulations, {members[winner]}!")
        print("You are the Master of Guessing!")
    else:
        print("The winners are:")
        for winner in winners:
            print(f"{members[winner]} guessed the number in {min_attempts} attempts!")
        print("All of the winners can play again to be the Master of Guessing!")

while True:
    runGame()
    agn = input("Do you want to play again? (y/n): ")
    if agn.lower() == 'y':
        print("Reinitializing the game...")
        print("--------------------")
    else:
        print("Closing the game...")
        break
