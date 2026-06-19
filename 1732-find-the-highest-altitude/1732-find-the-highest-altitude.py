class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        gains = 0

        for g in gain:
            gains += g
            res = max(res, gains)

        return res
