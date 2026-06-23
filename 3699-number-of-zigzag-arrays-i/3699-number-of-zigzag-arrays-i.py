class Solution:
    MOD = 10**9 + 7
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        m = r - l + 1
        dp = [0] + [1] * m
        
        for i in range(2, n + 1):
            pref = list(accumulate(dp))
            
            if i % 2 == 0:
                dp = [0] + pref[:-1]
            else:
                total = pref[-1]
                dp = [0] + [(total - x) % self.MOD for x in pref[1:]]
        
        return (sum(dp) % self.MOD * 2) % self.MOD
