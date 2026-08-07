class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        temp = t

        for i in range(2, 10):
            while temp % i == 0:
                temp //= i

        if temp > 1:
            return "-1"

        n = len(num)
        rem = [0] * (n + 1)
        rem[0] = t

        nums = list(num)
        pos = n - 1

        for i in range(n):
            if nums[i] == "0":
                pos = i
                break

            rem[i + 1] = rem[i] // math.gcd(rem[i], int(nums[i]))

        if rem[n] == 1:
            return num

        for i in range(pos, -1, -1):
            while True:
                nums[i] = chr(ord(nums[i]) + 1)

                if nums[i] > "9":
                    break

                need = rem[i] // math.gcd(rem[i], int(nums[i]))
                d = 9

                for j in range(n - 1, i, -1):
                    while need % d != 0:
                        d -= 1

                    need //= d
                    nums[j] = str(d)

                if need == 1:
                    return "".join(nums)

        ans = []
        temp = t

        for i in range(9, 1, -1):
            while temp % i == 0:
                ans.append(str(i))
                temp //= i

        ans = ans[::-1]
        return "1" * max(n + 1 - len(ans), 0) + "".join(ans)