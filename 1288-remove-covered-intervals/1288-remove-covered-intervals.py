class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        count = [1] * n

        for i in range(n):
            for j in range(n):
                if i != j and (count[i] and count[j]):
                    a = intervals[i][0]
                    b = intervals[i][1]
                    c = intervals[j][0]
                    d = intervals[j][1]

                    if a >= c and b <= d:
                        count[i] = 0
                    elif a <= c and b >= d:
                        count[j] = 0
        
        return sum(count)