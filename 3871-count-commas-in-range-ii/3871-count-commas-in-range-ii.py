class Solution:
    def countCommas(self, n: int) -> int:
        if n <= 999:
            return 0
        
        result = 0
        limit = [999, 999999, 999999999, 999999999999, 999999999999999]
        idx = 0

        if n > limit[idx]:
            result += n - limit[idx]
            idx += 1
        if n > limit[idx]:
            result += n - limit[idx]
            idx += 1
        if n > limit[idx]:
            result += n - limit[idx]
            idx += 1
        if n > limit[idx]:
            result += n - limit[idx]
            idx += 1
        if n > limit[idx]:
            result += n - limit[idx]
            idx += 1
        
        return result