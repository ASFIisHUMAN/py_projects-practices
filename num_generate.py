while True:
  print("Hello, what do you want to generate?")
  print("1. Prime Numbers")
  print("2. Non-Prime Numbers")
  print("3. Odd Numbers")
  print("4. Even Numbers")
  print("0 to Exit")


  def validate_input():
    while True:
        user_input = input("Enter your choice (1/2/3/4/0) : ")
        if user_input in ["1", "2", "3", "4"]:
            return int(user_input)
        elif user_input in ["0"]:
           print("\nThank you for using this program")
           exit()
        else:
            print("Invalid input. Please enter 0,1, 2, 3, or 4.")
  def range_input():
    while True:
        user_input = input("Enter the range : ")
        if user_input.isdigit() and 1 <= int(user_input) <= 1000:
            return int(user_input)
        else:
            print("Invalid input. Please enter a number")
  choice = validate_input()
  range_in=range_input()
  def pr_num(): 
    for num in range(0, range_in+1):
      if num > 1:
          for i in range(2, num):
              if (num % i) == 0:
                 break
          else:
              print(num)
  
  def non_pr_num():
    for num in range(0, range_in+1):
      for i in range(2, num):
          if num % i == 0:
              print(num)
              break

  def odd_num():
    for num in range(0, range_in+1):
      if num % 2 != 0:
        print(num)

  def even_num():
    for num in range(1, range_in+1):
      if num % 2 == 0:
        print(num)
  h="\n"
  if choice == 1:
    pr_num()
    print(h)
  elif choice == 2:
    non_pr_num()
    print(h)
  elif choice == 3:
    odd_num()
    print(h)
  elif choice == 4:
    even_num()
    print(h)
