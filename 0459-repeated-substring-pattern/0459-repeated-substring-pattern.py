class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)

        def check(x):
            init = s[:x]
            temp = x * 2
            valid = True

            for j in range(x, n, x):
                if temp <= n and s[j:temp] != init:
                    valid = False
                temp += x
            
            return valid 

        for i in range(1, n // 2 + 1):
            if n % i == 0:
                if check(i):
                    return True

        return False