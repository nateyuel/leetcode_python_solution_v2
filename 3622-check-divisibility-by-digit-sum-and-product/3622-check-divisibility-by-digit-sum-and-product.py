class Solution:
    def checkDivisibility(self, n: int) -> bool:
        d_sum = 0
        d_prod = 1
        m = n

        while m // 10 > 0:
            k = m % 10
            m //= 10
            d_sum += k
            d_prod *= k

        d_sum += m
        d_prod *= m

        return False if n % (d_sum + d_prod) else True