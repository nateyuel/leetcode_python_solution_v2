class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        c = 0

        while c < n:

            rem = 0
            idx = c
            cnt = 0

            while cnt < n:
                rem += gas[idx] - cost[idx]

                if rem < 0:
                    break

                idx = (idx + 1) % n
                cnt += 1

            if cnt == n:
                return c

            c += cnt + 1

        return -1