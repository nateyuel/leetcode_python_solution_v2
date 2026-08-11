class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prfx_len = 1
        num_set = set(nums)

        for prev, curr in zip(nums, nums[1:]):
            if curr == prev + 1:
                prfx_len += 1
            else:
                break

        tot = (nums[prfx_len - 1] + nums[0]) * prfx_len // 2
        while tot in num_set:
            tot += 1

        return tot