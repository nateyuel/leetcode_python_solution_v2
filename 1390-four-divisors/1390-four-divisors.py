class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        mp = defaultdict(int)

        def divisors(x):
            temp = set()

            for d in range(1, int(math.sqrt(x)) + 1):
                if x % d == 0:
                    if len(temp) == 4:
                        return 0

                    temp.add(d)
                    temp.add(x // d)

            if len(temp) == 4:
                return sum(temp)
            return 0

        res = 0

        for num in nums:
            if mp[num] == 0:
                curr_sum = divisors(num)
                if curr_sum == 0:
                    mp[num] = -1
                else:
                    mp[num] = curr_sum
                    res += curr_sum
            else:
                if mp[num] != -1:
                    res += mp[num]

        return res