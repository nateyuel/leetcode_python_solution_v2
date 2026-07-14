class Solution:
    MOD = 1000000007
    def subsequencePairCount(self, nums: List[int]) -> int:
        dp = {(0, 0): 1}

        for x in nums:
            ndp = defaultdict(int)

            for (a, b), cnt in dp.items():
                ndp[a, b] = (ndp[a, b] + cnt) % self.MOD
                ndp[gcd(a, x), b] = (ndp[gcd(a, x), b] + cnt) % self.MOD
                ndp[a, gcd(b, x)] = (ndp[a, gcd(b, x)] + cnt) % self.MOD

            dp = ndp

        return sum(cnt for (a, b), cnt in dp.items() if a == b and a) % self.MOD