balance = 0
takeLimit = 400
taken = 0
depLimit = 10000
deped = 0
history = ""

while True:
    userInput = input("Enter one of these options: deposit, withdraw, balance, history, exit --> ")
    userInput = userInput.strip()
    
    if userInput == "balance":
        print(balance)

    elif userInput == "deposit":
        try:
            dep = int(input("Enter the amount --> "))
        except ValueError:
            print("Enter positive numbers only.")
        else:
            if dep < 0:
                print("Enter positive numbers only.")
            elif deped + dep >= depLimit:
                print("Total amount of deposited money excels the daily limit.")
            else:
                balance += dep
                history += f"deposited: {dep}, balance: {balance}, "

    elif userInput == "exit":
        break

    elif userInput == "withdraw":
        try:
            wit = int(input("Enter the amount --> "))
        except ValueError:
            print("Enter positive numbers only.")
        else:
            if wit < 0:
                print("Enter positive numbers only.")
            elif wit > balance:
                print("Not enough money.")
            elif taken + wit >= takeLimit:
                print("Total amount of withdrawn money excels the daily limit.")
            else:
                balance -= wit
                taken += wit
                history += f"withdrawn: {wit}, balance: {balance}, "
    
    elif userInput == "history":
        print(history)

    else:
        print("Enter commands exactly as listed.")