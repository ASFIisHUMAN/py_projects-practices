# Initialize an empty set
my_set = set()

# Function to display menu
def display_menu():
    print("\nSet Operations Menu:")
    print("1. Display the current set")
    print("2. Add an element to the set")
    print("3. Remove an element from the set")
    print("4. Check if an element is present in the set")
    print("5. Union of two sets")
    print("6. Intersection of two sets")
    print("7. Difference of two sets")
    print("8. Symmetric difference of two sets")
    print("0 to Exit")

# Function to perform CRUD operations
def perform_operations():
    while True:
        display_menu()
      
        choice = input("Enter your choice: ")

        if choice == '2':  # Add an element
          element =input("Enter the element to add: ")
          if len(element.split())==1:
              my_set.add(element) 
          else:
              z= element.split(' ')
              my_set.update(z)
          if '' in my_set:
                my_set.remove('')
          print(f"{set(element.split())} has added to the set.")
        elif choice == '3':  # Remove an element
            element = input("Enter the element to remove: ")
            if element in my_set:
                print(element)
                my_set.remove(element)
                print(f"{element} removed from the set.")
            else:
                print(f"{element} is not present in the set.")
        elif choice == '4':  # Check if an element is present
            element = input("Enter the element to check: ")
            if element in my_set:
                print(f"{element} is present in the set.")
            else:
                print(f"{element} is not present in the set.")
        elif choice == '1':  # Display the set
            if not my_set:
                print("The set is empty.")
            else: 
                print("Current set: \n", my_set)
        elif choice == '5':  # Union of two sets
            other_set = set(input("Enter elements of the other set separated by space: ").split())
            print("Union of two sets:", my_set.union(other_set))
        elif choice == '6':  # Intersection of two sets
            other_set = set(input("Enter elements of the other set separated by space: ").split())
            print("Intersection of two sets:", my_set.intersection(other_set))
        elif choice == '7':  # Difference of two sets
            other_set = set(input("Enter elements of the other set separated by space: ").split())
            print("Difference of two sets:", my_set.difference(other_set))
        elif choice == '8':  # Symmetric difference of two sets
            other_set = set(input("Enter elements of the other set separated by space: ").split())
            print("Symmetric difference of two sets:", my_set.symmetric_difference(other_set))
        # Exit the program
        elif choice == '0':
            print("thanks for using this program \n Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

# start operations
perform_operations()
