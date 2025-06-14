import win32com.client as wincl
import random

speaker_number = 0
spk = wincl.Dispatch("SAPI.SpVoice")
vcs = spk.GetVoices()
# SVSFlag = 10
# print(vcs.Item (speaker_number) .GetAttribute ("Name")) # prints speaker's name
spk.Voice
spk.SetVoice(vcs.Item(speaker_number))

def say_w(str):
    print(str)
    spk.speak(str)

say_w("Welcome to the Rock Paper Scissor game.")
say_w("Play this game with your friends against A.I. and see who can score more.")
say_w("If you score more than 10000 points, You win the game.")
say_w("You have got 3 lives to play with.")
say_w("If you lose all of your lives the game is over.")
say_w("But! you can gain lives by winning every 4 times.")
say_w("win gives you 200 points, tie 100 points and lose takes 100 points from you.")

say_w("\nGuideline :")
say_w("write 1 to choose Rock")
say_w("write 2 to choose Paper")
say_w("write 3 to choose Scissor")
say_w("write 0 to choose to Quit")
say_w("After choosing press the enter key")

#input function to avoid errors
def valip():
    while True:
        spk.speak("Enter your choice")
        user_input = input("Enter your choice --> ")
        if user_input in ["1", "2", "3", "0"]:
            return int(user_input)
        else:
            say_w("Invalid input. Please write 1, 2, 3 or 0.")

#func to run game
def runG():
    say_w("The Game has started!")
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
            if(win == 0 and lose == 0 and tie == 0):
                return
            break
        if b==1:
            say_w("You choose Rock")
        elif b==2:
            say_w("You choose Paper")
        elif b==3:
            say_w("You choose Scissor")
        if c==1:
            say_w("Computer chooses Rock")
        elif c==2:
            say_w("Computer chooses Paper")
        elif c==3:
            say_w("Computer chooses Scissor")

        if(b==1 and c==3) or (b==2 and c==1) or (b==3 and c==2): 
           say_w("You win")  
           win+=1
           if win>=4 and win%4==0:
               life+=1
               say_w(f"You got an extra life, Your total life is {life}")
        elif b==c:
            say_w("It's a tie")
            tie+=1
        else:
            say_w("You loose")
            lose+=1
            life-=1
            if life<1:
                score=(win*2-lose+tie)*100
                say_w("You have no life left, Your game is over!")
                break
        score=(win*2-lose+tie)*100
        if score>=500 and score%500==0:
            say_w(f"Congratulations you have scored {score}")
    say_w(f"Your total score is {score}")
    say_w(f"You had {win} wins, {tie} ties and {lose} loses.")
    print(f"Win={win} Tie={tie} Lose={lose}")
    acc=0
    if win+lose+tie!=0:
        acc= str(win*100/(win+lose+tie))[:5]
    say_w(f"Your winning accuracy is {acc}%")


while True:
    runG()
    spk.speak("Do you want to play again? If you want then write y, if not write n or anything and press the enter key")
    a=input("Do you want to play again (y/n):")
    if a=="y" or a=='Y':
        say_w("Starting the game again...")
    else:
        break