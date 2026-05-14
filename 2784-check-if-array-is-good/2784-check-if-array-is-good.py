class Solution:
    def isGood(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False

        n = len(nums) - 1
        arr = [1 for i in range(n)]
        arr[-1] += 1

        for num in nums:
            if num > n:
                return False
            else:
                arr[num-1] -= 1
            
        for c in arr:
            if c != 0:
                return False
        
        return True