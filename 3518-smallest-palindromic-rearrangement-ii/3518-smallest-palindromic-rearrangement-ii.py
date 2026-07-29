class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        def count_combinations(n, r, limit):
            r = min(r, n - r)
            res = 1

            for i in range(1, r + 1):
                res = res * (n - i + 1) // i
                if res > limit:
                    return limit + 1

            return res

        half = len(s) // 2
        freq = [0] * 26

        for c in s[:half]:
            freq[ord(c) - ord('a')] += 1

        def count_permutations(left):
            ways = 1

            for count in freq:
                if count:
                    ways *= count_combinations(left, count, k)
                    if ways > k:
                        return ways
                    left -= count

            return ways

        result = []
        rank = 1

        for _ in range(half):
            for ch in range(26):
                if freq[ch] == 0:
                    continue

                freq[ch] -= 1
                ways = count_permutations(half - len(result) - 1)

                if rank + ways > k:
                    result.append(chr(ch + ord('a')))
                    break

                freq[ch] += 1
                rank += ways

        if len(result) != half:
            return ""

        middle = s[half] if len(s) % 2 else ""
        left = "".join(result)

        return left + middle + left[::-1]