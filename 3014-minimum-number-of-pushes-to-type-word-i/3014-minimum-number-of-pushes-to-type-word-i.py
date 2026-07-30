class Solution:
    def minimumPushes(self, word: str) -> int:
        d = len(word) // 8
        r = len(word) % 8

        return (((d * (d + 1)) // 2) * 8) + (d + 1) * r