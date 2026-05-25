class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        f = [0] * n
        pre = [0] * n
        f[0] = 1

        for i in range(minJump):
            pre[i] = 1

        for i in range(minJump, n):
            left = i - maxJump
            right = i - minJump

            if s[i] == "0":
                total = pre[right] - (0 if left <= 0 else pre[left - 1])
                f[i] = int(total != 0)

            pre[i] = pre[i - 1] + f[i]

        return bool(f[n - 1])