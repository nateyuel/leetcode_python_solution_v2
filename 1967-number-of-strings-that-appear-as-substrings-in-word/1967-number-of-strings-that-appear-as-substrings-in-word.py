class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0

        for pt in patterns:
            if pt in word:
                count += 1
        
        return count