class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        max_len = 0

        for i in range(n):
            store = defaultdict(int)
            valid = True
            for j in range(i, n):
                if store[s[j]] == 2:
                    max_len = max(max_len, j - i)
                    valid = False
                    break
                else:
                    store[s[j]] += 1

            if valid:
                max_len = max(max_len, n - i)
        
        return max_len