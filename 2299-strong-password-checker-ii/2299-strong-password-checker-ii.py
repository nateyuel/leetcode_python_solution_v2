class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        n = len(password)
        sc_dict = {char: True for char in "!@#$%^&*()-+"}
        at_least_8_ch = True if n >= 8 else False
        one_lc = False
        one_uc = False
        one_dg = False
        one_sc = False
        adj_smc = True

        for i in range(n):
            ch = password[i]
            if ch.isalpha():
                if ch.islower() and not one_lc:
                    one_lc = True
                elif ch.isupper() and not one_uc:
                    one_uc = True
            elif ch.isdigit() and not one_dg:
                one_dg = True
            elif ch in sc_dict:
                one_sc = True
            
            if i > 0 and ch == password[i-1]:
                adj_smc = False
        
        res = at_least_8_ch and one_lc and one_uc and one_dg and one_sc and adj_smc

        return res 
