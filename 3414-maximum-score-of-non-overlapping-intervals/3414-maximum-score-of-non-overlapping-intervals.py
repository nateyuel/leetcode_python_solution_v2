class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        arr = sorted(
            [(l, r, w, i) for i, (l, r, w) in enumerate(intervals)]
        )

        starts = [x[0] for x in arr]

        next_idx = [0] * n

        for i in range(n):
            l, r, w, idx = arr[i]

            lo, hi = i + 1, n

            while lo < hi:
                mid = (lo + hi) // 2

                if starts[mid] > r:
                    hi = mid
                else:
                    lo = mid + 1

            next_idx[i] = lo

        dp = [[None] * (n + 1) for _ in range(5)]

        for i in range(n + 1):
            dp[0][i] = (0, ())

        for k in range(1, 5):
            dp[k][n] = (0, ())

            for i in range(n - 1, -1, -1):
                skip = dp[k][i + 1]

                l, r, w, original_idx = arr[i]

                nxt = dp[k - 1][next_idx[i]]

                take_indices = tuple(
                    sorted((original_idx,) + nxt[1])
                )

                take = (
                    w + nxt[0],
                    take_indices
                )

                if take[0] > skip[0]:
                    dp[k][i] = take
                elif take[0] < skip[0]:
                    dp[k][i] = skip
                else:
                    dp[k][i] = min(take, skip, key=lambda x: x[1])

        return list(dp[4][0][1])