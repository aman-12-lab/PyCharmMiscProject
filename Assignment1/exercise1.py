def tester(givenstring="Too short"):
    print(givenstring)

while True:
    text = input("Write something (quit ends): ")
    if text == "quit":
        break
    if len(text) < 10:
        tester()
    else:
        tester(text)