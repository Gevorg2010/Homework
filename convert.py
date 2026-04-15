def convert(num, base1, base2):
    #cases
    if base1 == base2:
        return num
    
    if num == "0":
        return num

    #convert to decimal
    decimalNum = 0
    for i in range(len(num)):
        decimalNum += base1 ** (len(num) - 1 - i) * int(num[i])

    #convert to base2
    res = ""
    while decimalNum > 0:
        res += str(decimalNum % base2)
        decimalNum //= base2
    res = res[::-1]
    
    return res
            
print(convert(input("Input the number: "), int(input("Input the base1: ")), int(input("Input the base2: "))))