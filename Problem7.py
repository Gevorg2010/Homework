def f(arr, k):
    add = 0
    res = 0
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            add = sum(arr[i:j+1])
            if add == k:
                res += 1
                add = 0
                break
            if add > k:
                add = 0
                break
    return res
print(f(list(map(int, input("Iput the array: ").split())), int(input("Input k: "))))
        
