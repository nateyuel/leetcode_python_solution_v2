class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        max_num = float("-inf")
        min_num = float("inf")
        idx_1 = 0
        idx_2 = 0

        for idx, num in enumerate(nums):
            if num > max_num:
                idx_1 = idx
                max_num = num
            if num < min_num:
                idx_2 = idx
                min_num = num

        min_idx = min(idx_1, idx_2)
        max_idx = max(idx_1, idx_2)

        res = min(max_idx + 1, n - min_idx, min_idx + 1 + n - max_idx)

        return res