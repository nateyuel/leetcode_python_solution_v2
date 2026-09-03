class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        smallest_odd = float("inf")
        smallest_even = float("inf")

        for num in nums1:
            if num % 2 == 1:
                smallest_odd = min(smallest_odd, num)
            else:
                smallest_even = min(smallest_even, num)
        
        if smallest_odd == float("inf") or smallest_even == float("inf"):
            return True
        
        odd_count = 0
        even_count = 0
        n = len(nums1)

        for num in nums1:
            if num % 2 == 1:
                odd_count += 1
                if num - smallest_odd >= 1:
                    even_count += 1
            else:
                even_count += 1
                if num - smallest_odd >= 1:
                    odd_count += 1
            
        result = True if odd_count == n or even_count == n else False

        return result
