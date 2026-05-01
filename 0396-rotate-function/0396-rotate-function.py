class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        f = 0
        n = len(nums)
        numSum = sum(nums)

        for i, num in enumerate(nums):
            f += i * num

        res = f
        for i in range(n - 1, 0, -1):
            f = f + numSum - n * nums[i]
            res = max(res, f)
            
        return res