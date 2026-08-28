class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        row = int(coordinates[1])
        col = coordinates[0]

        if (row % 2 == 0 and col in ('a', 'c', 'e', 'g')) or \
        (row % 2 == 1 and col in ('b', 'd', 'f', 'h')):
            return True
        
        return False