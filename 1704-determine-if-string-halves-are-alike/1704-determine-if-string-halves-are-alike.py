class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        left_vc = 0
        right_vc = 0
        n = len(s)

        for i in range(n//2):
            ch = s[i].lower()
            if ch in ('a', 'e', 'i', 'o', 'u'):
                left_vc += 1
        
        for i in range(n//2, n):
            ch = s[i].lower()
            if ch in ('a', 'e', 'i', 'o', 'u'):
                right_vc += 1

        return left_vc == right_vc     