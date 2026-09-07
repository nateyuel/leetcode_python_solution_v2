class Solution:
    def isValid(self, word: str) -> bool:
        min_3 = len(word) >= 3
        one_vowel = False
        one_consonant = False
        no_other = True

        for ch in word:
            if ch.isalpha() or ch.isnumeric():
                if ch.isalpha():
                    if ch.lower() in ('a', 'e', 'i', 'o', 'u'):
                        one_vowel = True
                    else:
                        one_consonant = True
            else:
                no_other = False
            
        return min_3 and one_vowel and one_consonant and no_other