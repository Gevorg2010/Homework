def fibonachi(n,x,y,res):
    proxima = x + y
    x = y
    y = proxima
    if proxima == n:
        return res
    if proxima > n:
        return -1
    return fibonachi(n,x,y,res+1)

print(fibonachi(int(input("Input a number: ")),1,1,3))