def long(arr):
        res = 0
        for i in arr:
            res += 1
        return res
        
def rotate(matrix):
    res = [[] for i in range(long(matrix))]
    
    for i in range(long(matrix)-1,-1,-1):
        for j in range(long(matrix)):
            res[j].append(matrix[i][j])
        
    return res

print(rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))
