class Solution:
    def maxProduct(self, n: int) -> int:
        dg_1 = 0
        dg_2 = 0

        while n > 0:
            if dg_1 > dg_2:
                if n % 10 > dg_2:
                    dg_2 = n % 10
            else:
                if n % 10 > dg_1:
                    dg_1 = n % 10

            n //= 10
        
        return dg_1 * dg_2

        
        
        