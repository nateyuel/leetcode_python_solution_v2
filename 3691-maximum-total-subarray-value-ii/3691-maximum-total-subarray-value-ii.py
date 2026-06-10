class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        lg = (n + 1).bit_length()

        mx = [nums[:]]
        mn = [nums[:]]

        for j in range(1, lg):
            step = 1 << (j - 1)
            mx.append([max(mx[j - 1][i], mx[j - 1][i + step])
                       for i in range(n - (1 << j) + 1)])
            mn.append([min(mn[j - 1][i], mn[j - 1][i + step])
                       for i in range(n - (1 << j) + 1)])

        def value(l, r):
            k = (r - l + 1).bit_length() - 1
            p = 1 << k
            return (
                max(mx[k][l], mx[k][r - p + 1])
                - min(mn[k][l], mn[k][r - p + 1])
            )

        h = []

        for l in range(n):
            heappush(h, (-value(l, n - 1), l, n - 1))

        ans = 0

        while k:
            v, l, r = heappop(h)
            ans -= v
            k -= 1

            if r > l:
                heappush(h, (-value(l, r - 1), l, r - 1))

        return ans