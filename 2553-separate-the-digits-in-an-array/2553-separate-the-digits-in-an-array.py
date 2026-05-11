class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        joined = "".join([str(num) for num in nums])
        return list(map(int, joined))

        