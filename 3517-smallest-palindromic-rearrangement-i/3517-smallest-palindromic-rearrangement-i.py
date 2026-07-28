class Solution:
    def smallestPalindrome(self, s: str) -> str:
        counter = Counter(s)
        elements = sorted(list(counter.keys()))

        conc = ""
        odd_occur = ""

        for ch in elements:
            if len(s) % 2 == 1:
                if counter[ch] % 2 == 1:
                    odd_occur = ch
            conc += (ch * (counter[ch] // 2))
        
        return conc + odd_occur + conc[::-1]
