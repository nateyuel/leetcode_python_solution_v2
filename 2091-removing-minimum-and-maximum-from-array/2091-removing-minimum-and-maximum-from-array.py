class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        idx_1 = nums.index(min(nums)) 
        idx_2 = nums.index(max(nums))

        min_idx = min(idx_1, idx_2)
        max_idx = max(idx_1, idx_2)

        res = min(max_idx + 1, n - min_idx, min_idx + 1 + n - max_idx)

        return res