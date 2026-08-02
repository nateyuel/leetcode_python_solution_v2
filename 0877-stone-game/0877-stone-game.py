class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)

        @lru_cache(None)
        def dp(l, r):
            if l > r:
                return 0
            
            turn = (r - l - n) % 2

            if turn == 1:
                return max(piles[l] + dp(l+1, r), piles[r] + dp(l, r-1))
            else:
                return max(dp(l+1, r) - piles[l], dp(l, r-1) - piles[r])

        return dp(0, n-1) > 0