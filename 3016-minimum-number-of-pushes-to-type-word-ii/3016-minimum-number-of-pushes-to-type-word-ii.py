class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = Counter(word)
        unique_letters = sorted(counter, reverse=True, key=counter.get)

        min_res = 0
        r = 0
        c = 1

        for let in unique_letters:
            if c == 1:
                r += 1

            min_res += counter[let] * r

            if c == 8:
                c = 1
            else:
                c += 1
        
        return min_res