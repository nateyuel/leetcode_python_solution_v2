class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda item:(item[0], -item[1]))
        last = (intervals[0])

        count = len(intervals)
        n = len(intervals)

        for i in range(1, n):
            start, end = intervals[i]
            if start >= last[0] and end <= last[1]:
                count -= 1
            else:
                last = (intervals[i])
        
        return count