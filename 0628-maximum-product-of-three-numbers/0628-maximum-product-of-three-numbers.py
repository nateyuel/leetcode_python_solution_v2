class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        product1 = 1
        product2 = 1

        for i in nums[-3:]:
            product1 *= i

        for j in nums[0:2]:
            product2 *= j
            
        return max(product1, product2*nums[-1])