class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        present = set(nums)
        result = []
        max_num = max(nums)
        min_num = min(nums)

        for num in range(min_num + 1, max_num):
            if num not in present:
                result.append(num)
        
        return result