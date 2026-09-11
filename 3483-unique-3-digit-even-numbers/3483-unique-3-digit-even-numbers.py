class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        result = 0
        n = len(digits)
        check = set()

        for i in range(n):
            if digits[i] > 0:
                for j in range(n):
                    for k in range(n):
                        if i != j and i != k and j != k:
                            num = digits[i] * 100 + digits[j] * 10 + digits[k]
                            if num % 2 == 0 and num not in check:
                                result += 1
                                check.add(num)
        
        return result


