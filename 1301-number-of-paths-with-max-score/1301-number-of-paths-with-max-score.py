class Solution:
    MOD = 10**9 + 7
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        def update_cell(curr_row: int, curr_col: int, prev_row: int, prev_col: int) -> None:
            if prev_row >= board_size or prev_col >= board_size or max_score[prev_row][prev_col] == -1:
                return
          
            if board[curr_row][curr_col] in "XS":
                return
          
            if max_score[prev_row][prev_col] > max_score[curr_row][curr_col]:
                max_score[curr_row][curr_col] = max_score[prev_row][prev_col]
                path_count[curr_row][curr_col] = path_count[prev_row][prev_col]

            elif max_score[prev_row][prev_col] == max_score[curr_row][curr_col]:
                path_count[curr_row][curr_col] += path_count[prev_row][prev_col]
      
        board_size = len(board)
      
        max_score = [[-1] * board_size for _ in range(board_size)]
      
        path_count = [[0] * board_size for _ in range(board_size)]
      
        max_score[-1][-1] = 0
        path_count[-1][-1] = 1
      
        for row in range(board_size - 1, -1, -1):
            for col in range(board_size - 1, -1, -1):
                update_cell(row, col, row + 1, col)      
                update_cell(row, col, row, col + 1)      
                update_cell(row, col, row + 1, col + 1) 
              
                if max_score[row][col] != -1 and board[row][col].isdigit():
                    max_score[row][col] += int(board[row][col])
      
        if max_score[0][0] == -1:
            return [0, 0]
        else:
            return [max_score[0][0], path_count[0][0] % self.MOD]
