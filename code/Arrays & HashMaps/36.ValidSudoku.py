# Problem: Two Sum: https://leetcode.com/problems/two-sum
# Difficulty: Easy
# Time Taken: 10 min
# Attempts: 1
# Hints Used: No
# Notes: Use a dictionnary with set values to store unique numbers of each cols, rows and squares. If the element is found in it return false. To manage square we use: squares[(r // 3, c // 3)] that identifies each 3x3 box by its row and column group and keeps track of seen digits in that box.
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)  

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if ( board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True