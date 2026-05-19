class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        n = len(mat)
        m = len(mat[0])

        prefix = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                prefix[i + 1][j + 1] = (
                    mat[i][j]
                    + prefix[i][j + 1]
                    + prefix[i + 1][j]
                    - prefix[i][j]
                )

        def get_sum(r1, c1, r2, c2):
            return (
                prefix[r2 + 1][c2 + 1]
                - prefix[r1][c2 + 1]
                - prefix[r2 + 1][c1]
                + prefix[r1][c1]
            )

        ans = 0

        for size in range(1, min(n, m) + 1):

            found = False

            for i in range(n - size + 1):
                for j in range(m - size + 1):

                    total = get_sum(
                        i,
                        j,
                        i + size - 1,
                        j + size - 1
                    )

                    if total <= threshold:
                        ans = size
                        found = True
                        break

                if found:
                    break

        return ans