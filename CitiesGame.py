import csv

with open('worldcities.csv', mode='r') as f:
    file = csv.DictReader(f)
    cities = []
    mentioned = []

    #list with all cities
    for row in file:
        cities.append(row["city"])

    #game
        count = 0
        latest = "&"
    while True:
        
        userInput = input("Input a city name: ")
        userInput = userInput.strip()
        do = True
        
        #wrong input
        if userInput not in cities and userInput not in mentioned:
            print("There isn't any city with this name.")
            do = False
        
        #stars with wrong latter
        if userInput[0].lower() != latest[-1] and count > 1 and userInput in cities and do:
            print("The city name should start whith the last letter of previous one.")
            do = False

        #mentioned
        if userInput in mentioned:
            print("It has already been mentioned.")
            do = False
        
        if userInput in cities and do:
            count += 1
            for i in range(len(cities)): 
                if userInput[-1] == cities[i][0].lower():
                    print(cities[i])
                    latest = cities[i]
                    mentioned.append(cities[i])
                    mentioned.append(userInput)
                    cities.pop(i)
                    break
