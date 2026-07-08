class Solution:
    MOD = 10 ** 9 + 7
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)

        pos = []
        digits = []

        pref_sum = [0] * (n + 1)

        for i, ch in enumerate(s):
            d = ord(ch) - 48
            pref_sum[i + 1] = pref_sum[i] + d

            if d:
                pos.append(i)
                digits.append(d)

        m = len(digits)

        if m == 0:
            return [0] * len(queries)

        pw = [1] * (m + 1)
        inv = [1] * (m + 1)

        inv10 = pow(10, self.MOD - 2, self.MOD)

        for i in range(1, m + 1):
            pw[i] = pw[i - 1] * 10 % self.MOD
            inv[i] = inv[i - 1] * inv10 % self.MOD

        pref_num = [0] * (m + 1)
        pref_digit = [0] * (m + 1)

        for i, d in enumerate(digits):
            pref_num[i + 1] = (pref_num[i] * 10 + d) % self.MOD
            pref_digit[i + 1] = pref_digit[i] + d

        ans = []

        for l, r in queries:
            L = bisect_left(pos, l)
            R = bisect_right(pos, r)

            if L == R:
                ans.append(0)
                continue

            cnt = R - L

            x = (pref_num[R] - pref_num[L] * pw[cnt]) % self.MOD
            sm = pref_digit[R] - pref_digit[L]

            ans.append(x * sm % self.MOD)

        return ans