import random
print("Welcome to the Rock Paper Scissor game.")
print("play this game with your and see who can score more")
print("If you score more than 10000 points. You win the game.")
print("You have got 3 lives to play with.")
print("If you lose all of your lives the game is over.")
print("But you can gain lives by winning every 4 times.")
print("win gives you 200 points, tie 100 points and lose takes 100 points")
print("Guide :")
print("1) Rock")
print("2) Paper")
print("3) Scissor")
print("0) to Quit")

#input function to avoid errors
def valip():
    while True:
        user_input = input("Enter your choice -->")
        if user_input in ["1", "2", "3", "0"]:
            return int(user_input)
        else:
            print("Invalid input. Please enter 1 or 2 or 3 or 0.")

#func to run game
def runG():
    print("The Game is started")
    win=0
    lose=0
    tie=0
    score=0
    life=3
    
    while True:
        b=valip()
        z=[1, 2, 3]
        c= random.choice(z)
        if b==0:
            break
        if b==1:
            print("You choose Rock")
        elif b==2:
            print("You choose Paper")
        elif b==3:
            print("You choose Scissor")
        if c==1:
            print("Computer chooses Rock")
        elif c==2:
            print("Computer chooses Paper")
        elif c==3:
            print("Computer chooses Scissor")

        if(b==1 and c==3) or (b==2 and c==1) or (b==3 and c==2): 
           print("You win")  
           win+=1
           if win>=4 and win%4==0:
               life+=1
               print(f"You got an extra life, Your total life is {life}")
        elif b==c:
            print("It's a tie")
            tie+=1
        else:
            print("You loose")
            lose+=1
            life-=1
            if life<1:
                score=(win*2-lose+tie)*100
                print("You have no life left, Your game is over!")
                break
        score=(win*2-lose+tie)*100
        if score>=500 and score%500==0:
            print(f"Congratulations you have scored {score}")
    print(f"Your total score is {score}")
    print(f"Win={win} Tie={tie} Lose={lose}")
    acc=0
    if win+lose+tie!=0:
        acc= str(win*100/(win+lose+tie))[:5]
    print(f"Your winning accuracy is {acc}%")


while True:
    runG()
    a=input("Do you want to play again (y/n):")
    if a=="y" or a=='Y':
        print("Starting the game again...")
    else:
        break