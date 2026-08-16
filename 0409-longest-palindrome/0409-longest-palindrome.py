class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        mid = ""
        result = 0

        for ch, frq in count.items():
            if mid == "" and frq % 2 != 0:
                mid = ch
                result += 1

            result += (frq // 2) * 2

        return result