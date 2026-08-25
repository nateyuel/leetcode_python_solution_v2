class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        store = set(nums)
        idx = 1

        while True:
            if k * idx not in store:
                return k * idx
            else:
                idx += 1