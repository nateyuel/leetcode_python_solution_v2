class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        s = set()

        for n1 in nums:
            for n2 in nums:
                s.add(n1 ^ n2)
        
        l = list(s)
        s = set()

        for xor in l:
            for num in nums:
                s.add(xor ^ num)
        
        return len(s)