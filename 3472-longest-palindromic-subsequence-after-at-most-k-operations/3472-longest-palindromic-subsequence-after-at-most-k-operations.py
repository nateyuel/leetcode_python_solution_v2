class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        n = len(s)

        def cost(a: str, b: str) -> int:
            d = abs(ord(a) - ord(b))
            return min(d, 26 - d)

        dp = [[[0] * (k + 1) for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for kk in range(k + 1):
                dp[i][i][kk] = 1

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                c = cost(s[i], s[j])

                for kk in range(k + 1):

                    best = max(
                        dp[i + 1][j][kk],
                        dp[i][j - 1][kk]
                    )

                    if c <= kk:
                        best = max(
                            best,
                            2 + dp[i + 1][j - 1][kk - c]
                        )

                    dp[i][j][kk] = best

        return dp[0][n - 1][k]