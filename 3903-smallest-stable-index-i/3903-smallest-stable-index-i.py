class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        min_list = nums.copy()
        max_list = nums.copy()

        for i in range(1, n):
            max_list[i] = max(max_list[i-1], nums[i])

        for i in range(n - 2, - 1, - 1):
            min_list[i] = min(min_list[i+1], nums[i])
        
        result = - 1

        for i in range(n):
            score = max_list[i] - min_list[i]
            if score <= k:
                result = i
                break 
                        
        return result
