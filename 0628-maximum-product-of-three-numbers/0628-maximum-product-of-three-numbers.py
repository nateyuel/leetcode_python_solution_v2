class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        prd_1 = 1
        prd_2 = 1

        for i in nums[-3:]:
            prd_1 *= i

        for j in nums[0:2]:
            prd_2 *= j

        return max(prd_1, prd_2*nums[-1])