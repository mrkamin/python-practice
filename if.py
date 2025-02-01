command = ""

while command != quit:
    command = input('>')
    if command.lower() == "start":
        print("Car started")
    elif command.lower() == "stop":
        print("Car Stoped")
    elif command.lower() == "help":
        print("""
Start - to start the car
Stop - to stop the car
quit - to exit
        """)
    elif command.lower() == "quit":
        print("exit")
        break
    else:
        print("I don't understand...")
