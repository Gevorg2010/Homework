def fact(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * fact(x-1)
    
def ItsFact(num,res):
    if fact(res) > num:
        return -1
    if fact(res) == num:
        return res
    return ItsFact(num, res+1)

print(ItsFact(int(input("Input a number: ")),1))