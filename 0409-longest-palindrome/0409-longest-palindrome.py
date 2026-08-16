class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        result = 1 if any(frq % 2 for frq in count.values()) else 0

        for frq in count.values():
            if frq % 2:
                result += frq - 1
            else:
                result += frq

        return result