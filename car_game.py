command = ""
while True:
    command=input("> ").lower()
    if command == "start":
        print("Car started...")
    elif command == "stop":
        print("Car stopped...")
    elif command == "help":
        print('''
start-aadaff
stop-rgrgrgrgrwg
quit-skjjsfjfşıs
        ''')
    elif command == "quit":
        break
    else:
        print("Does not understand")