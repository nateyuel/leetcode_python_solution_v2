class Solution:
    MOD = 10**9 + 7
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        m = r - l + 1

        dp_0 = [1] * m
        dp_1 = [1] * m

        for _ in range(n - 1):
            sum_0 = list(accumulate(dp_0, initial=0))
            sum_1 = list(accumulate(dp_1, initial=0))

            dp_0 = [x % self.MOD for x in sum_1[:-1]]

            s0_m = sum_0[-1]
            dp_1 = [(s0_m - x) % self.MOD for x in sum_0[1:]]

        return (sum(dp_0) + sum(dp_1)) % self.MOD