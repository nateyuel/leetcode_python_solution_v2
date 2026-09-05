class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        length = len(nums)
        min_list = nums.copy()
        max_list = nums.copy()

        for idx, num in enumerate(nums):
            if idx > 0:
                max_list[idx] = max(max_list[idx-1], max_list[idx])
        
        for idx in range(length - 2, -1, -1):
            min_list[idx] = min(min_list[idx], min_list[idx + 1])
        
        min_idx = -1

        for idx in range(length):
            if max_list[idx] - min_list[idx] <= k:
                min_idx = idx
                break
        
        return min_idx
