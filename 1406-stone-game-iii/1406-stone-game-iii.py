class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = [0, 0, 0]

        for i in range(len(stoneValue) - 1, -1, -1):
            take = best = -float("inf")

            for j in range(i, min(i + 3, len(stoneValue))):
                take = stoneValue[j] if j == i else take + stoneValue[j]
                best = max(best, take - dp[(j + 1) % 3])

            dp[i % 3] = best

        if dp[0] > 0:
            return "Alice"
        if dp[0] < 0:
            return "Bob"
        return "Tie"