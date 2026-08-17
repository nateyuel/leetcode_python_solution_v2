class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        count_cap = 0
        n = len(word)

        for ch in word:
            if ch.isupper():
                count_cap += 1
        
        if n == count_cap or count_cap == 0:
            return True
        if count_cap == 1 and word[0].isupper():
            return True

        return False