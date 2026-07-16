class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefix_gcd = [nums[0]]
        mxi = nums[0]
        n = len(nums)

        for i in range(1, n):
            mxi = max(mxi, nums[i])
            prefix_gcd.append(gcd(nums[i], mxi))

        prefix_gcd.sort()
        res = 0

        for j in range(0, n // 2):
            res += gcd(prefix_gcd[j], prefix_gcd[-(j+1)])
        
        return res