class Solution:
    def smallestPalindrome(self, s: str) -> str:
        counter = Counter(s)
        elements = sorted(list(counter.keys()))

        conc_ch = ""
        odd_occur = ""

        for ch in elements:
            if len(s) % 2 == 1:
                if counter[ch] % 2 == 1:
                    odd_occur = ch
            conc_ch += (ch * (counter[ch] // 2))
        
        return conc_ch + odd_occur + conc_ch[::-1]
