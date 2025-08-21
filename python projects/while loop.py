#atm simulation
balance = 1000

user_input= (input("press 1 for deposit, 2 for withdraw, 3 for check balance, exit to quit").upper())

while user_input != "exit":
    if user_input =='D':
        amount = int(input("enter the amount to deposit"))
        balance += amount
        print("you have deposited" , amount ,"rupees in your account")
    elif user_input == 'W':
        amount = int(input("enter the amount to withdraw"))
        if(amount <= balance):
            balance -= amount
            print("you have withdrawn",amount, "rupees from your account")
        else :
            print("you dont have sufficient balance")
    elif user_input == 'c':
        print("the current balance is", balance)

    else:
        print("invalid input")
        user_input = input("press 'D' for deposit, 'W' for withdrawn, 'c' for checking the balance , exit to quit").upper()








