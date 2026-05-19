class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        if nums1[0] > nums2[-1] or nums1[-1] < nums2[0]:
            return -1
        
        if nums1[0] == nums2[0] or nums1[0] == nums2[-1]:
            return nums1[0]
            
        if nums1[-1] == nums2[0]:
            return nums2[0]

        i = 0
        j = 0

        n = len(nums1)
        m = len(nums2)

        while i < n and j < m:
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

            if i < n and nums1[i] > nums2[-1]:
                return -1

            if j < m and nums1[-1] < nums2[j]:
                return -1
        
        return -1