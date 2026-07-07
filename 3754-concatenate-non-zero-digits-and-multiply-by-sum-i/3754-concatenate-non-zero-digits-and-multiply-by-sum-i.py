class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0

        dig_sum = 0
        dig_conc = ""

        while n >= 10:
            curr = n % 10
            if curr != 0:
                dig_sum += curr
                dig_conc = str(curr) + dig_conc
            
            n //= 10
        
        if n != 0:
                dig_sum += n
                dig_conc = str(n) + dig_conc

        return int(dig_conc) * dig_sum