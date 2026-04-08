def long(arr):
        res = 0
        for i in arr:
            res += 1
        return res
        
def where(arr, target):
        for i in range(long(arr)):
            if arr[i] == target:
                return i
        return -1
        
def valid(s):
    s = list(s)   
    opens="([{"
    closes=")]}"
    length = long(s)
    i = -1
    while i < length-1:
        i += 1
        curr = where(opens,s[i])
        if curr == -1:
            return False
        j = i+1
        
        while j < length:
            if curr == where(closes,s[j]):
                s1 = s[i+1:j]
                if not valid(s1):
                    return False
                del s[j]
                del s[i]
                length = long(s)
                i = -1
            j += 1
            
    return long(s) == 0
        
print(valid(input("Input the string: ")))
