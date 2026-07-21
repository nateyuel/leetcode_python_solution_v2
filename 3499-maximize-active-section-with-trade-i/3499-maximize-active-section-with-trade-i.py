class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones = s.count("1")
        blocks = []

        i, n = 0, len(s)

        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1

            if s[i] == "0":
                blocks.append(j - i)

            i = j

        if len(blocks) < 2:
            return ones

        gain = 0
        for i in range(len(blocks) - 1):
            gain = max(gain, blocks[i] + blocks[i + 1])

        return ones + gain