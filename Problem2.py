def often(nums):
    res = {}
    arr = list(set(nums))
    for i in range(len(arr)):
        res[arr[i]] = nums.count(arr[i])
    return list(res)[list(res.values()).index(max(list(res.values())))]
print(often(list(map(int, input("Input the array: ").split()))))
