class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        arr1 = list(map(str, arr1))
        arr2 = list(map(str, arr2))
        store = set()

        for cand in arr1:
            for i in range(len(cand), -1, -1):
                if cand[:i] in store:
                    break  
                store.add(cand[:i])
        
        max_length = 0

        for cand in arr2:
            for i in range(len(cand), -1, -1):
                if cand[:i] in store:
                    max_length = max(max_length, abs(i))
                    break

        return max_length