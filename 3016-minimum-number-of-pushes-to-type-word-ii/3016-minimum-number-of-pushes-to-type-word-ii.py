class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = Counter(word)
        unique_letters = sorted(counter, reverse=True, key=counter.get)

        min_res = 0
        phase = 0
        count = 1

        for let in unique_letters:
            if count == 1:
                phase += 1

            min_res += counter[let] * phase

            if count == 8:
                count = 1
            else:
                count += 1
        
        return min_res