class Solution:
    def maxProduct(self, n: int) -> int:
        m1 = 0
        m2 = 0

        while n > 0:
            k = n % 10
            if m1 > m2:
                if k > m2:
                    m2 = k
            else:
                if k > m1:
                    m1 = k

            n //= 10
        
        return m1 * m2

        
        
        