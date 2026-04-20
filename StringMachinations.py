import time

string = ""
prestring = [""]
count = -1

while True:
    userInput = input("Enter one of these options: type, delete, print, undo, redo, exit. --> ")
    userInput = userInput.strip()

    if userInput == "type":
        typ = input("Enter a string --> ")
        string += typ
        prestring.append(string)
    
    elif userInput == "delete":
        try:
            k = int(input(f"Enter number of letters to delete (max {len(string)}) --> "))
        except TypeError:
            print("Enter positive numbers only.")
            time.sleep(1)
            k = int(input(f"Enter number of letters to delete (max {len(string)}) --> "))
        else:
            if k < 0:
                print("Enter positive numbers only.")
                time.sleep(1)
            elif k > len(string):
                print(f"The number should be up to {len(string)}.")
                time.sleep(1)
            else:
                string = string[0:len(string)-k]
                if count == -1:
                    prestring.append(string)
                else:
                    prestring.insert(count+1, string)
                    count += 1

    elif userInput == "print":
        print(string)
        time.sleep(1)

    elif userInput == "undo":
        if abs(count) < len(prestring):
            count -= 1
            string = prestring[count]

    elif userInput == "redo":
        if count < -1:
            count += 1
            string = prestring[count]

    elif userInput == "exit":
        break

    else:
        print("Enter commands exactly as listed.")
        time.sleep(1)
