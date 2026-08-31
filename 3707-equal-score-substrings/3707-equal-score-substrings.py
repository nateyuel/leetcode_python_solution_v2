class Solution:
    def scoreBalance(self, s: str) -> bool:
        n = len(s)
        scores = [ord(s[i]) - 96 for i in range(n)]
        tot_sum = sum(scores)
        curr_sum = 0

        for score in scores:
            curr_sum += score
            if curr_sum * 2 == tot_sum:
                return True
        
        return False
