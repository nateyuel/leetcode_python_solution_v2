class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        m = max(costs)
        counts = [0] * (m + 1)

        for cst in costs:
            counts[cst] += 1

        max_ics = 0

        for cost in range(1, len(counts)):
            if coins < cost:
                break

            count = counts[cost]
            curr = coins // cost
            possible = min(count, curr)

            max_ics += possible
            coins -= (possible * cost) 
        
        return max_ics



