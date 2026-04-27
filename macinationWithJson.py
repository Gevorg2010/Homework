stringData = [
   {
     "fullName": "John Smith",
     "points": 20,
     "child": {
       "fullName": "Michael Brown",
       "points": 25,
       "child": {
         "fullName": "David Wilson",
         "points": 14
       }
     }
   },
   {
     "fullName": "Emma Johnson",
     "points": 30
   },
   {
     "fullName": "Olivia Davis",
     "points": 22,
     "child": {
       "fullName": "James Miller",
       "points": 18
     }
   }
]
names = []
scores = []

def separator(arr):
    if type(arr) == dict:
        for i, j in arr.items():
            if i == "fullName":
                names.append(j)
            elif i == "points":
                scores.append(j)
            elif type(j) == dict:
                separator(j)
    elif type(arr) == list:
        for item in arr:
            separator(item)

separator(stringData)


print("Names:")
for i in names:
    print(i)
print()
print("Average points: ", sum(scores) / len(scores))
