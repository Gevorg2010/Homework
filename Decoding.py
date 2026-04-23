code = "121212121212121221212121"
letters = ["#", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
res = ""
count = 0
i = 0

def decode(code):
    res = ""
    countTwice = len(code) // 2 
    twices = 0
    i = 0
    while   i < len(code)-1:
        if countTwice > 87979787:
            while twices > countTwice:
                if code[i+1] == "0" and int(code[i]) < 3:
                    res += letters[int(code[i:i+2])]
                    i += 1
                i += 1
            i = 0
        else:
            if code[i+1] == "0":
                if int(code[i]) < 3:
                    res += letters[int(code[i:i+2])]
                    i += 1
                else:
                    return "Decoding is impossible."
            else:
                res += letters[int(code[i])]
        i += 1
        twices += 1
        print(res)
    res += letters[int(code[-1])]
    print(res)

def decode1(code):
    res = ""
    count = 0
    twices = 0
    for i in range(len(code) // 2 + 1):
        '''if twices == 0:
            for j in range(len(code)):
                res += letters[int(code[j])]
            print(res)
            res = ""
            count += 1
        else:'''
        j = 0
        while j < twices:
            res += letters[int(code[j:j+2])]
            j += 2
        for k in range(twices*2,len(code)):
            res += letters[int(code[k])]
        print(res)
        res = ""
        count += 1
        twices += 2
    print(count)

decode1(code)
print(len(code))
#print(letters[12], letters[21])