print("Ke Hobe Cotipoti. the game")
def instant_quit():
    print("Your total won is ",taka,"taka")
    print(r)
    exit()
def validate_input():
  while True:
      user_input = input("Enter your answer (1/2/3/4) or 0 to quit : ")
      if user_input in ["1", "2", "3", "4"]:
          return int(user_input)
      elif user_input in ["0"]:
         instant_quit()
      else:
          print("Invalid input. Please enter 0,1, 2, 3, or 4.")

q1="1. What is the capital city of Bangladesh?"
q2="2. Which river is known as the lifeline of Bangladesh?"
q3="3. Which Bangladeshi city is known as the 'City of Mosques'?"
q4="4. Which political party led the liberation movement of Bangladesh in 1971?"
q5="5. Which Nobel laureate was born in Bangladesh and won the Nobel Peace Prize in 2006?"
q6="6. Which famous mangrove forest is located in Bangladesh?"
q7="7. What is the national flower of Bangladesh?"
q8="8. Which Bangladeshi cricketer became the first to score a double century in a Test match?"
q9="9. What is the national bird of Bangladesh?"
q10="10. In which year did Bangladesh gain independence from Pakistan?"
q11="11. Which Bangladeshi river is the longest?"
q12="12. What is the traditional dress of Bangladeshi women called?"
q13="13. Which Bangladeshi filmmaker won the Palme d'Or at the Cannes Film Festival?"
q14="14. Which Bangladeshi poet was awarded the Nobel Prize in Literature in 1913?"
q15="15. Which Bangladeshi politician served as the Prime Minister for a record three terms?"

r= "please rate the game and send your ratting and score to the admin at instagram id: @unknown.midfielder"

ans1 =  ["1. Dhaka", "2. Chittagong", "3. Rajshahi", "4. Khulna"]
ans2 =  ["1. Brahmaputra", "2. Ganges", "3. Jamuna", "4. Meghna"]
ans3 =  ["1. Dhaka", "2. Chittagong", "3. Sylhet", "4. Khulna"]
ans4 =  ["1. Awami League", "2. Bangladesh Nationalist Party", "3. Jatiya Party", "4. Jamaat-e-Islami"]
ans5 =  ["1. Muhammad Yunus", "2. Malala Yousafzai", "3. Kailash Satyarthi", "4. Shirin Ebadi"]
ans6 =  ["1. Sundarbans", "2. Chittagong Hill Tracts", "3. Cox's Bazar", "4. Sylhet"]
ans7 =  ["1. Water Lily", "2. Lotus", "3. Jasmine", "4. Rose"]
ans8 =  ["1. Shakib Al Hasan", "2. Mushfiqur Rahim", "3. Tamim Iqbal", "4. Mominul Haque"]
ans9 =  ["1. Oriental Magpie-Robin", "2. Kingfisher", "3. Parrot", "4. Peacock"]
ans10 =  ["1. 1971", "2. 1947", "3. 1980", "4. 1991"]
ans11 =  ["1. Jamuna", "2. Padma", "3. Meghna", "4. Brahmaputra"]
ans12 =  ["1. Sari", "2. Salwar Kameez", "3. Lungi", "4. Panjabi"]
ans13 =  ["1. Satyajit Ray", "2. Ritwik Ghatak", "3. Tareque Masud", "4. Anwar Hossain"]
ans14 =  ["1. Rabindranath Tagore", "2. Kazi Nazrul Islam", "3. Jasimuddin", "4. Jibanananda Das"]
ans15 =  ["1. Sheikh Hasina", "2. Khaleda Zia", "3. Sheikh Mujibur Rahman", "4. Hussain Muhammad"]

taka=0
print(q1)
print(ans1)
l = validate_input()
if(l==1):
  taka+=1000
  print("Correct answer! You have won",taka,"taka")
  print(q2)
  print(ans2)
  l = validate_input()

else:
  print(r)
  print("Wrong answer! Your total won is ",taka,"taka")
  exit()

if(l==3):
  taka+=1000
  print("Correct answer! You have won",taka,"taka")
  print(q3)
  print(ans3)
  l = validate_input()
else:
  print(r)
  print("Wrong answer! Your total won is ",taka,"taka")
  exit()

if(l==1):
  taka+=1000
  print("Correct answer! You have won",taka,"taka")
  print(q4)
  print(ans4)
  l = validate_input()
else:
  print(r)
  print("Wrong answer! Your total won is ",taka,"taka")
  exit()

if(l==1):
  taka+=1000
  print("Correct answer! You have won",taka,"taka")
  print(q5)
  print(ans5)
  l = validate_input()
else:
  print(r)
  print("Wrong answer! Your total won is ",taka,"taka")
  exit()

if(l==1):
  taka+=1000
  print("Correct answer! You have won",taka,"taka")
  print(q6)
  print(ans6)
  l = validate_input()
else:
  print(r)
  print("Wrong answer! Your total won is ",taka,"taka")
  exit()

if(l==1):
  taka+=1000
  print("Correct answer! You have won",taka,"taka")
  print(q7)
  print(ans7)
  l = validate_input()
else:
  print(r)
  print("Wrong answer! Your total won is ",taka,"taka")
  exit()

if(l==1):
  taka+=1000
  print("Correct answer! You have won",taka,"taka")
  print(q8)
  print(ans8)
  l = validate_input()
else:
  print(r)
  print("Wrong answer! Your total won is ",taka,"taka")
  exit()

if(l==1):
  taka+=1000
  print("Correct answer! You have won",taka,"taka")
  print(q9)
  print(ans9)
  l = validate_input()
else:
  print(r)
  print("Wrong answer! Your total won is ",taka,"taka")
  exit()

if(l==1):
  taka+=1000
  print("Correct answer! You have won",taka,"taka")
  print(q10)
  print(ans10)
  l = validate_input()
else:
  print(r)
  print("Wrong answer! Your total won is ",taka,"taka")
  exit()

if(l==1):
  taka+=1000
  print("Correct answer! You have won",taka,"taka")
  print(q11)
  print(ans11)
  l = validate_input()
else:
  print(r)
  print("Wrong answer! Your total won is ",taka,"taka")
  exit()

if(l==4):
  taka+=1000
  print("Correct answer! You have won",taka,"taka")
  print(q12)
  print(ans12)
  l = validate_input()
else:
  print(r)
  print("Wrong answer! Your total won is ",taka,"taka")
  exit()

if(l==2):
  taka+=1000
  print("Correct answer! You have won",taka,"taka")
  print(q13)
  print(ans13)
  l = validate_input()
else:
  print(r)
  print("Wrong answer! Your total won is ",taka,"taka")
  exit()

if(l==3):
  taka+=1000
  print("Correct answer! You have won",taka,"taka")
  print(q14)
  print(ans14)
  l = validate_input()
else:
  print(r)
  print("Wrong answer! Your total won is ",taka,"taka")
  exit()

if(l==1):
  taka+=1000
  print("Correct answer! You have won",taka,"taka")
  print(q15)
  print(ans15)
  l = validate_input()
else:
  print(r)
  print("Wrong answer! Your total won is ",taka,"taka")
  exit()

if(l==1):
  taka+=11000
  print("Correct answer! Your total won is",taka,"taka")
  print("Congratulations! You have won the game")
  print(r)
else:
  print(r)
  print("Wrong answer! Your total won is ",taka,"taka")
  exit()
