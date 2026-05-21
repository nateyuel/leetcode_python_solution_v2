class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        arr1 = list(map(str, arr1))
        arr2 = list(map(str, arr2))
        store = set()

        for cand in arr1:
            for i in range(len(cand)):
                store.add(cand[:i+1])
        
        max_length = 0

        for cand in arr2:
            for i in range(len(cand)):
                if cand[:i+1] in store:
                    max_length = max(max_length, i+1)
        
        return max_length