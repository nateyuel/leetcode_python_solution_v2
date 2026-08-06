class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        
        while True:
            prd = 1
            m = n
            while m >= 10:
                prd *= (m % 10)
                m //= 10

            prd *= m

            if prd % t == 0:
                return n
            else:
                n += 1
        
        