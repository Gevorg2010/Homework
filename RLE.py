def rle(s):
    res = ""
    s = list(s)
    s.append("^")
    for i in range(len(s)-1):
        if i+1<len(s):
            if s[i] == s[i+1]:
                count = 1
                j = i
                while s[j] == s[j+1] and j < len(s)-1:
                    count += 1
                    j += 1
                
                s = s[0:i+1] + s[j+1:len(s)]
                s[i] = str(count) + s[i]
    s.pop()
    
    for i in s:
        res += i
    
    return res
            
print(rle(input("Input the string: ")))
