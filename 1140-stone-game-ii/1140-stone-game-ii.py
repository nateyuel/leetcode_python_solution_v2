class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suf = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suf[i] = suf[i + 1] + piles[i]

        @lru_cache(None)
        def dp(i, m):
            if i >= n:
                return 0

            best = 0
            for x in range(1, 2 * m + 1):
                if i + x > n:
                    break
                best = max(best, suf[i] - dp(i + x, max(m, x)))

            return best

        return dp(0, 1)