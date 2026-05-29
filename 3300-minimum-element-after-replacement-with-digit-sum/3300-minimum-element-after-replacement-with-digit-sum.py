class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_elem = float("inf")

        for num in nums:
            dig_sum = 0

            while num >= 10:
                dig_sum += num % 10
                num //= 10
            
            dig_sum += num

            min_elem = min(min_elem, dig_sum)

        return min_elem
        
