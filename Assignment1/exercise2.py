#In the second exercise the idea is to create a small grocery shopping list with the list datastructure.

shopping_list = []

while True:
    choice = input("Would you like to\n(1)Add or\n(2)Remove items or\n(3)Quit?: ")

    if choice == "1":
        shopping_list.append(input("What will be added?: "))

    elif choice == "2":
        print("There are", len(shopping_list), "items in the list.")
        i = int(input("Which item is deleted?: "))
        if i >= 0 and i < len(shopping_list):
            shopping_list.pop(i)
        else:
            print("Incorrect selection.")

    elif choice == "3":
        print("The following items remain in the list:")
        for x in shopping_list:
            print(x)
        break

    else:
        print("Incorrect selection.")