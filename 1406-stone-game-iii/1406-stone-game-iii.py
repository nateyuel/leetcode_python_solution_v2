class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)

        @lru_cache(None)
        def dp(i):
            if i == n:
                return 0

            take = 0
            res = -float("inf")

            for j in range(i, min(i + 3, n)):
                take += stoneValue[j]
                res = max(res, take - dp(j + 1))

            return res

        score = dp(0)

        if score > 0:
            return "Alice"
        if score < 0:
            return "Bob"
        return "Tie"