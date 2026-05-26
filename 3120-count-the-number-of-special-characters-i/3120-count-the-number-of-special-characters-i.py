class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        store = set()
        count = 0

        for l in word:
            if l in store:
                continue
            if l == l.upper():
                if l.lower() in store:
                    count += 1
            if l == l.lower():
                if l.upper() in store:
                    count += 1
                
            store.add(l)

        return count