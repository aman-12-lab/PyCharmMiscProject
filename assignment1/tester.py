#This exercise tests out the default values of parameters

def tester(givenstring="Too short"):
    print(givenstring)

while True:
    user_input = input("Write something (quit ends): ")

    if user_input == "quit":
        break
    elif len(user_input) < 10:
        tester()  # default value
    else:
        tester(user_input)

