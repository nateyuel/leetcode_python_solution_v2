class Solution:
    def oddString(self, words: List[str]) -> str:
        n = len(words)
        m = len(words[0])
        freq = defaultdict(int)
        first_diff = ()

        for i in range(n):
            diff = ()
            for j in range(m-1):
                diff = diff + (ord(words[i][j+1]) - ord(words[i][j]),)
            
            freq[diff] += 1

            if i == 0:
                first_diff = first_diff + diff
            elif i > 1 and freq[diff] == 1:
                return words[i]

        if freq[first_diff] == 1:
            return words[0]
        else:
            return words[1]