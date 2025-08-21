age = int(input("enter age"))
citizenship = input("are you a citizen? enter true/false").upper()
print("age is \n citizenship", age, citizenship)

if citizenship != "true" and age >=18:
    print("you cannot vote , as you are not citizen")
else:
    if citizenship == 'true' and age >=18:
        print("you are voting")
    else:
        difference = 18 - age
        print("you are enter 18, you have to wait for ",difference,"years")







