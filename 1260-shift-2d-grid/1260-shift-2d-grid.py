class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        while k > 0:
            carry = grid[-1][-1]

            for i in range(m):
                row = [carry] + grid[i][:-1]
                carry = grid[i][-1]
                grid[i] = row

            k -= 1

        return grid