class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        memo = {}

        def dfs(left, right):
            if left > right:
                return 0

            if (left, right) in memo:
                return memo[(left, right)]

            take_left = nums[left] + min(
                dfs(left + 2, right),
                dfs(left + 1, right - 1),
            )

            take_right = nums[right] + min(
                dfs(left, right - 2),
                dfs(left + 1, right - 1),
            )

            memo[(left, right)] = max(take_left, take_right)
            return memo[(left, right)]

        score = dfs(0, len(nums) - 1)
        return score >= sum(nums) - score