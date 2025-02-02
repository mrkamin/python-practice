command = ""
started = False

while True:
    command = input(">").lower()
    if command == "start":
        if started:
            print("Car is already started...")
        else:
            started = True
            print("Car is started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car is stopped!")
    elif command == "help":
        print("""
start - to start the car!
stop - to stop the car!
quit - to exit the game!
        """)
    elif command == 'quit':
        break
    else:
        print("I don't understand!")