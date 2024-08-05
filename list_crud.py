# importing pyperclip for copy function
import pyperclip
# Declare an empty list
my_list = []

# display the current list
def showlist():
    if not my_list:
        print("The list is empty.")
    else:
        print("Current list: \n", my_list)

#  add an item to the list
def add():
    item = input("Enter the item to add: ")
    my_list.append(item)
    print("Item added successfully.")

# update an item in the list 
def updl():
    if not my_list:
        print("The list is empty. Nothing to update.")
    else:
        showlist()
        index = int(input("Enter the item num to update: "))
        if index-1 < 0 or index-1 >= len(my_list):
            print("Invalid index.")
        else:
            new_item = input("Enter the new item value: ")
            my_list[index] = new_item
            print("Item updated successfully.")
# copy function  
try:
    def copy_list():
        if not my_list:
            print("The list is empty. Nothing to copy.")
        else:
             pyperclip.copy("\n".join(my_list))
             print("your list has been copied to clipboard")
except ModuleNotFoundError as e:
       print(e)
# delete an item from the list
def delete():
    if not my_list:
        print("The list is empty. Nothing to delete.")
    else:
        showlist()
        index = int(input("Enter the item num to delete: "))
        if index-1 < 0 or index-1 >= len(my_list):
            print("Invalid num.")
        else:
            deleted_item = my_list.pop(index-1)
            print("Item '{}' deleted successfully.".format(deleted_item))

# loop to exicute
while True:
    print("\nMenu:")
    print("1. Display list")
    print("2. Add item")
    print("3. Update item")
    print("4. Delete item")
    print("5. Copy")
    print("6. Exit")

    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == "1":
        showlist()
    elif choice == "2":
        add()
    elif choice == "3":
        updl()
    elif choice == "4":
        delete()
    elif choice == "5":
        copy_list()
    elif choice == "6":
        print("goodbye")
        break
    else:
        print("Invalid choice. Please write 1/2/3/4/5/6.")

