'''
Եթե առաջին թիվը փոքր է երկրորդից, մեծ թիվ ենք սահմանում երկրորդը և վերջում պատասխանին դիմացից ավելացնում ենք -։
Թվերը շրջած լցնում ենք ցուցակի մեջ, տարրերը հերթով հանում ենք
Եթե տարրերի տարբերությունը 0-ից փոքր է, այդ թվի փոխարեն գրում ենք տարրերի տարբերությանը գումարած 10 և հաջորդից հանում ենք 1 եթե այն մեծ է 0-ից, հակառակ դեպքում գնում ենք առաջ մինչև հանդիպենք 0-ից տարբեր թիվ, բոլոր 0-ները 9-երով փոխարինելով։
Վերջում նորից շրջում ենք տողի մեջ։
'''

def dif(a, b):
    
    if a=="0" and b=="0":
        return 0
    
    la = len(a)
    lb = len(b)
    minus = False
    
    if la == lb:
        for i in range(la):
            if a[i] > b[i]:
                bigger = a
                smaller = b
                break
            else:
                bigger = b
                smaller = a
                minus = True
                break
    else:
        if la > lb:
            bigger = a
            smaller = b
        else:
            minus = True
            bigger = b
            smaller = a
    
    arb = [int(bigger[i]) for i in range(len(bigger)-1, -1, -1)]
    ars = [int(smaller[i]) for i in range(len(smaller)-1, -1, -1)]
    arr = arb
    res = ""
    lm = min(la, lb)
    
    for i in range(lm):
        
        if arb[i] < ars[i]:
            arr[i] = 10+arb[i]-ars[i]
            if arr[i+1] != 0:
                arr[i+1] -= 1
            else:
                j = i+1
                while arr[j] == 0 and j < lm:
                    
                    arr[j] = 9
                    j += 1
                arr[j] -= 1
                
                    
        else:
            arr[i] = arb[i] - ars[i]

    if minus:
        arr.append("-")
    
    for i in range(len(arr)-1, -1, -1):
        res += str(arr[i])
      
    return res

print(dif(input("N1: "), input("N2: ")))
