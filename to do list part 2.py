#Daniel Marquez
#1/12

shoppingList = ["beans", "rice", "chicken", "tomatoes", "potatoes"]

def to_Do():
    print("Shopping list")
    print(shoppingList)
    print("Choose an option for your to-do list, pick a number from 1-8")  
    print("1. Add a task to your list \n2. View your list \n3. Mark a task as completed \n4. Remove a task from your list \n5. Remove all items from your list \n6. Sort the list alphabetically \n7. Print the # of items on the list \n8. Exit the program")
    option = int(input("Option: "))

    if option == 1:
        x = input("Add another food: ")
        shoppingList.append(x)
        print(shoppingList)
    
    if option == 2: 
        print(shoppingList)

    if option == 3:
        x = input("Enter a food to be marked: ")
        i = shoppingList.index(x)
        shoppingList[i] = x + "[X]"
        print(shoppingList)

    if option == 4: 
        x = input("Enter a food to be removed: ")
        shoppingList.remove(x)
        print(shoppingList)
    
    if option == 5:
        shoppingList.clear()
        print(shoppingList)
    
    if option == 6:
        shoppingList.sort()
        print(shoppingList)
    
    if option == 7:
        x = int(shoppingList.__len__())
        print(x)

    if option == 8:
        quit()


#main
to_Do()