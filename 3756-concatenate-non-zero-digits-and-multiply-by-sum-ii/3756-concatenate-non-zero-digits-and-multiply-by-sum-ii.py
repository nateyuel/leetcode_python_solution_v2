MOD = 10 ** 9 + 7
pow10 = [1] * 100001

for i in range(1, 100001):
    pow10[i] = pow10[i - 1] * 10 % MOD


class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)

        pref_sum = [0] * (n + 1)
        pref_num = [0] * (n + 1)
        pref_cnt = [0] * (n + 1)

        for i, ch in enumerate(s):
            d = int(ch)

            pref_sum[i + 1] = pref_sum[i] + d
            pref_cnt[i + 1] = pref_cnt[i] + (d != 0)

            if d:
                pref_num[i + 1] = (pref_num[i] * 10 + d) % MOD
            else:
                pref_num[i + 1] = pref_num[i]

        res = []

        for l, r in queries:
            curr_sum = pref_sum[r + 1] - pref_sum[l]
            length = pref_cnt[r + 1] - pref_cnt[l]

            curr_num = (
                pref_num[r + 1]
                - pref_num[l] * pow10[length]
            ) % MOD

            res.append(curr_num * curr_sum % MOD)

        return res