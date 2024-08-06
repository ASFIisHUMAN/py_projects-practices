import sys

print("Welcome to Ke Hobe Cotipoti. the game")
print("This is a cotipoti game where you have to answer the questions. \nYou will get taka for each correct answer. \nThe game ends when you answer 15 questions or you choose to quit instantly.")
print("If you answer all of them correctly you will get 1 crore taka.")
print("you will win money by choosing the correct answer. \nyou will lose some money by choosing the wrong answer")
print("At early stage if you choose wrong you will loose all of them")
print("here isthe chart of taka by games\n questions    per-win    per-Loses\n ---------   ---------   ---------\n  1 <-> 2     30000$        All   \n     3        40000$        All   \n  4 <-> 6     150000$     90000$  \n  7<-->10     450000$     300000$ \n  11<->12     1300000$    900000$ \n  13<->14     1750000$    1100000$\n   final      2100000$    4000000$\n")
print("Now lets start ")
print("------------------------------")

r = "please rate the game and send your rating to the admin at instagram id: @Asfi.js"
taka = 0

def instant_quit():
    global appe, taka
    print("quitting challenge...")
    if appe < 1:
        print(r)
    else:
        print(f"Your total appearances are {appe}")
        print(f"Your total winning money is {taka} taka")
        print(r)
    sys.exit()

def exiting():
    global taka
    if 0 <= (appe-1) < 2:
            taka = 0
    elif (appe-1) == 2:
            taka =0
    elif 3 <= (appe-1) < 6:
            taka -= 90000
    elif 6 <= (appe-1) < 10:
            taka -= 300000
    elif 10 <= (appe-1) < 12:
            taka -= 900000
    elif 12 <= (appe-1) < 14:
            taka -= 1100000
    else:
        taka -= 4000000
    print(f"Wrong answer! Your total winning is {taka} taka")
    print(r)
    sys.exit()

def validate_input():
    while True:
        user_input = input("Choose the answer (1/2/3/4) or 0 to instant quit--> ")
        if user_input in ["1", "2", "3", "4"]:
            return int(user_input)
        elif user_input == "0":
            instant_quit()
        else:
            print("Invalid input. Please enter 0, 1, 2, 3, or 4.")

qna = [
    ["1. What is the capital city of Bangladesh?", "1. Dhaka, 2. Chittagong, 3. Rajshahi, 4. Khulna", 1],
    ["2. Which river is known as the lifeline of Bangladesh?", "1. Brahmaputra, 2. Ganges, 3. Jamuna, 4. Meghna", 3],
    ["3. Which Bangladeshi city is known as the 'City of Mosques'?", "1. Khulna, 2. Chittagong, 3. Sylhet, 4. Dhaka", 4],
    ["4. Which political party led the liberation movement of Bangladesh in 1971?", "1. Jamaat-e-Islami, 2. Bangladesh Nationalist Party, 3. Jatiya Party, 4. Awami League", 4],
    ["5. Which Nobel laureate was born in Bangladesh and won the Nobel Peace Prize in 2006?", "1. Muhammad Yunus, 2. Malala Yousafzai, 3. Kailash Satyarthi, 4. Shirin Ebadi", 1],
    ["6. Which famous mangrove forest is located in Bangladesh?", "1. Chittagong Hill Tracts, 2. Sundarbans, 3. Cox's Bazar, 4. Sylhet", 2],
    ["7. What is the national flower of Bangladesh?", "1. Jasmine, 2. Lotus, 3. Water Lily, 4. Rose", 3],
    ["8. Which Bangladeshi cricketer became the first to score a double century in a Test match?", "1. Shakib Al Hasan, 2. Mushfiqur Rahim, 3. Tamim Iqbal, 4. Mominul Haque", 1],
    ["9. What is the national bird of Bangladesh?", "1. Kingfisher, 2. Oriental Magpie-Robin, 3. Parrot, 4. Peacock", 2],
    ["10. In which year did Bangladesh gain independence from Pakistan?", "1. 1971, 2. 1947, 3. 1980, 4. 1991", 1],
    ["11. Which Bangladeshi river is the longest?", "1. Jamuna, 2. Padma, 3. Meghna, 4. Brahmaputra", 4],
    ["12. What is the traditional dress of Bangladeshi women called?", "1. Sari, 2. Salwar Kameez, 3. Lungi, 4. Panjabi", 2],
    ["13. Which Bangladeshi filmmaker won the Palme d'Or at the Cannes Film Festival?", "1. Satyajit Ray, 2. Ritwik Ghatak, 3. Tareque Masud, 4. Anwar Hossain", 3],
    ["14. Which Bangladeshi poet was awarded the Nobel Prize in Literature in 1913?", "1. Kazi Nazrul Islam, 2. Rabindranath Tagore, 3. Jasimuddin, 4. Jibanananda Das", 2],
    ["15. Which Bangladeshi politician served as the Prime Minister for a record three terms?", "1. Sheikh Hasina, 2. Khaleda Zia, 3. Sheikh Mujibur Rahman, 4. Hussain Muhammad", 1]
]

appe = 0

for i in range(len(qna)):
    appe += 1
    print(qna[i][0])
    print(qna[i][1])
    ans = validate_input()
    if ans == qna[i][2]:
        print("Correct!")
        if 0 <= i < 2:
            taka += 30000
            print("You got 30000 taka")
        elif i == 2:
            taka += 40000
            print("You got 40000 taka")
        elif 3 <= i < 6:
            taka += 150000
            print("You got 150000 taka")
        elif 6 <= i < 10:
            taka += 450000
            print("You got 450000 taka")
        elif 10 <= i < 12:
            taka += 1300000
            print("You got 1300000 taka")
        elif 12 <= i < 14:
            taka += 1750000
            print("You got 1750000 taka")
        else:
            taka = 1000000
            print("Congratulations!")
            print("You won the game.")
            print(f"Your total amount of money is {taka} taka")
            print(r)
            sys.exit()
    else:
        exiting()
        break
