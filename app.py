driver_choice = ""
started = False
while True:
    driver_choice = input("> ").upper()
    if driver_choice == "HELP":
        print("Start = to start the car")
        print("Stop = to stop the car")
        print("quit = to exit")
    elif driver_choice.upper() == "START":
        if not started:
            print("Car started")
            started = True
        else:
            print("Car already started")
    elif driver_choice.upper() == "STOP":
        if started:
            print("Car is stopped !")
            started = False
        else:
            print("car already stopped")

    elif driver_choice.upper() == "QUIT":
        print("Bye Bye")
        break
    else:
        print("I don't understand!")
