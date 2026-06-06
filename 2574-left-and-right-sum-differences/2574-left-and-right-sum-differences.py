class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_sum = [0] * n
        right_sum = [0] * n

        for i in range(1, n):
            left_sum[i] = left_sum[i-1] + nums[i-1]

        for i in range(-2, -n-1, -1):
            right_sum[i] = right_sum[i+1] + nums[i+1]
        
        res = [0] * n

        for i in range(n):
            res[i] = abs(left_sum[i] - right_sum[i])
        
        return res
