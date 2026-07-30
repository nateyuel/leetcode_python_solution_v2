class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        d = n // 8
        r = n % 8

        res = (((d * (d + 1)) // 2) * 8) + (d + 1) * r

        return res