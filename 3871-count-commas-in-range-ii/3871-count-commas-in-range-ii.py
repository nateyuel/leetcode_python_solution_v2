class Solution:
    def countCommas(self, n: int) -> int:
        if n <= 999:
            return 0
        
        result = 0

        if n > 999:
            result += n - 999
        if n > 999999:
            result += n - 999999
        if n > 999999999:
            result += n - 999999999
        if n > 999999999999:
            result += n - 999999999999
        if n > 999999999999999:
            result += n - 999999999999999
        
        return result