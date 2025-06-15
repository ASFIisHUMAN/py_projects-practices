# windows only
import win32com.client as wincl # please run:  pip install --upgrade pywin32   in shell to download the package
import random
import sys
from time import sleep

speaker_number = 0
spk = wincl.Dispatch("SAPI.SpVoice")
vcs = spk.GetVoices()
# SVSFlag = 10
# print(vcs.Item (speaker_number) .GetAttribute ("Name")) # prints speaker's name
spk.Voice
spk.SetVoice(vcs.Item(speaker_number))

print("Do you prefer sound? (YES/NO) \n-write y or yes as YES \n-write anything or n as NO \n-write 0 to quit instantly")
ver=input("--> ")
if(ver=='0'):
    print("Closing the game...")
    sys.exit()
elif(ver.lower() == 'y' or ver.lower() == "yes"):
    print("______________________________________\n")
    def show_match_result(str):
        print(str)
        spk.speak(str[:11])
        
    def say_w(str):
        print(str)
        spk.speak(str)

    def ask_w(str):
        spk.speak(str)
        inp= input(f"{str} --> ")
        return inp

else:
    print("______________________________________\n")
    def show_match_result(str):
        print(str)

    def say_w(str):
        print(str)
        sleep(0.35)

    def ask_w(str):
        inp= input(f"{str} --> ")
        return inp

say_w("Welcome to the Rock Paper Scissor game.")
say_w("Play this game with your friends against A.I. and see who can score more.")
say_w("You have got 3 lives to play with.")
say_w("If you lose all of your lives the game is over.")
say_w("But! you can gain lives by winning every 4 times.")
say_w("Win gives you 200 points, draw gives 100 points and lose takes 100 points from you.")

say_w("\nGuideline : to choose")
say_w("write 1 for Rock")
say_w("write 2 for Paper")
say_w("write 3 for Scissor")
say_w("write 0 to Quit")
say_w("After writing press the enter key")

r_p_s=['Rock' , 'Paper' , 'Scissor']

#input function to avoid errors
def valip():
    while True:
        user_input = ask_w("Enter your choice")
        if user_input in ["1", "2", "3", "0"]:
            return int(user_input)
        else:
            say_w("Invalid input. Please write 1, 2, 3 or 0.")


#func to run game
def runG():
    say_w("The Game has started!")
    congrats_step=500
    win=0
    lose=0
    draw=0
    score=0
    life=3
    
    while True:
        b=valip() # player's choice

        c= random.choice([1, 2, 3]) # computer's choice

        if b==0:
            if(win == 0 and lose == 0 and draw == 0):
                say_w("Closing the game...")
                sys.exit()
            break

        say_w(f"You choose {r_p_s[b-1]}")
        say_w(f"Computer chooses {r_p_s[c-1]}")

        if(b==1 and c==3) or (b==2 and c==1) or (b==3 and c==2): 
           score+=200
           win+=1
           show_match_result(f"You win!                [score = {score}]")
           if win>=4 and win%4==0:
               life+=1
               say_w(f"You got an extra life, Your total life is {life}")
        elif b==c:
            score+=100
            draw+=1
            show_match_result(f"It's a draw!            [score = {score}]")
        else:
            score-=100
            lose+=1
            life-=1
            show_match_result(f"You loose!             [score = {score}]")
            if life<1:
                say_w("You have no life left, Your game is over!")
                break

        if score>=congrats_step:
            congrats_step+=500
            say_w(f"Congratulations you have scored {score}")

    say_w(f"Your total score is {score}")
    say_w(f"You had {win} wins, {draw} draws and {lose} loses.")
    print(f"Win={win} draw={draw} Lose={lose}")
    acc= str(win*100/(win+lose+draw))[:5]
    say_w(f"Your winning accuracy is {acc}%")


while True:
    runG()
    a=input("Do you want to play again (y/n):")
    if a.lower() == "y" or a.lower() == 'yes':
        say_w("Starting the game again...")
    else:
        break