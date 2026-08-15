class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)

        i = 0
        j = 0

        valid = [False] * n

        while i < n and j < m:
            if s[i] ==  t[j]:
                valid[i] = True
                i += 1
                j += 1
            else:
                j += 1
        
        return all(valid)