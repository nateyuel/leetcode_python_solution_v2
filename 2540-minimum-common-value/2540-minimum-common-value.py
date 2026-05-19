class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        mp = defaultdict(int)

        for num in nums1:
            mp[num] = 1
        
        for num in nums2:
            if mp[num] == 1:
                return num
        
        return -1