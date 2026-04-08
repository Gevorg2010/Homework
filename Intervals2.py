def intervalsIntersection(intervals,newInterval):
    intervals.append(newInterval)
    intervals.sort()
    
    def correctIntervals(intervals):
        for i in range(long(intervals)-1):
            if intervals[i][1] >= intervals[i+1][0]:
                return True
        return False
        
    def long(arr):
        res = 0
        for i in arr:
            res += 1
        return res
    
    lenght = long(intervals)-1
    i = 0
    while correctIntervals(intervals):
        if intervals[i][1] >= intervals[i+1][0]:
            replace = [intervals[i][0],intervals[i+1][1]]
            intervals.pop(i)
            intervals.pop(i)
            intervals.insert(i, replace)
            lenght = long(intervals)-1
    return intervals
       
            
print(intervalsIntersection([[1,3],[6,9]], [2,5]))
