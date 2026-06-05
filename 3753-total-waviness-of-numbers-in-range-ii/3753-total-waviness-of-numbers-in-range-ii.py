class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def solve(x: int) -> int:
            if x < 100:
                return 0

            s = str(x)

            @cache
            def dfs(i, a, b, tight, lead):
                if i == len(s):
                    return 1, 0

                total_cnt = total_wav = 0
                limit = int(s[i]) if tight else 9

                for d in range(limit + 1):
                    nlead = lead and d == 0

                    cnt, wav = dfs(
                        i + 1,
                        b,
                        -1 if nlead else d,
                        tight and d == limit,
                        nlead,
                    )

                    add = (
                        not nlead
                        and a >= 0
                        and b >= 0
                        and ((a < b > d) or (a > b < d))
                    )

                    total_cnt += cnt
                    total_wav += wav + add * cnt

                return total_cnt, total_wav

            return dfs(0, -1, -1, True, True)[1]

        return solve(num2) - solve(num1 - 1)