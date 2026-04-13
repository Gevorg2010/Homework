'''
Թվերը շրջած լցնում ենք ցուցակի մեջ, տարրերը հերթով գումարում ենք։ Եթե տարրերի գումարը 9-ից մեծ է, այդ թվի փոխարեն գրում ենք տարրերի գումարից հանած 10 և հաջորդին գումարում ենք 1։
Վերջում նորից շրջում ենք տողի մեջ։
'''

def summ(a, b):
    if a=="0" and b=="0":
        return 0
        
    arr = []
    la = len(a)
    lb = len(b)
    ara = [int(a[i]) for i in range(len(a)-1, -1, -1)]
    arb = [int(b[i]) for i in range(len(b)-1, -1, -1)]
    res = ""
    lm = min(la, lb)
    
    if la > lb:
        arr = ara
    else:
        arr = arb
        
    for i in range(lm):
        
        if ara[i]+arb[i] > 9:
            if i+1==len(arr):
                arr.append(0)
            arr[i] = ara[i]+arb[i]-10
            arr[i+1] += 1
        else:
            arr[i] = ara[i]+arb[i]

    if arr[-1]==0:
        arr.append(1)
    
    for i in range(len(arr)-1, -1, -1):
        res += str(arr[i])
      
    return res

print(summ(input("N1: "), input("N2: ")))
