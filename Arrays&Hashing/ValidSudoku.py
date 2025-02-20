"""
https://neetcode.io/problems/valid-sudoku
"""
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row
        for row in board:
            row_dict: dict = {}
            for cell in row:
                if not cell == ".":
                    if row_dict.get(cell) is None:
                        row_dict[cell] = cell
                    else:
                        return False
        # column
        for i in range(9):
            column_dict: dict = {}
            column = [row[i] for row in board]
            for cell in column:
                if not cell == ".":
                    if column_dict.get(cell) is None:
                        column_dict[cell] = cell
                    else:
                        return False
        # 3x3
        for i in range(3):
            for j in range(3):
                square_dict: dict = {}
                square = [board[3 * i + k][3 * j + l] for k in range(3) for l in range(3)]
                for cell in square:
                    if not cell == ".":
                        if square_dict.get(cell) is None:
                            square_dict[cell] = cell
                        else:
                            return False
        return True


if __name__ == '__main__':
    solution: Solution = Solution()
    board_test = [
        ["1", "2", ".", ".", "3", ".", ".", ".", "."],
        ["4", ".", ".", "5", ".", ".", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", ".", "3"],
        ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
        [".", ".", ".", "8", ".", "3", ".", ".", "5"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", ".", ".", ".", ".", ".", "2", ".", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "8"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    print(solution.isValidSudoku(board_test))
    board_test = [
        ["1", "2", ".", ".", "3", ".", ".", ".", "."],
        ["4", ".", ".", "5", ".", ".", ".", ".", "."],
        [".", "9", "1", ".", ".", ".", ".", ".", "3"],
        ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
        [".", ".", ".", "8", ".", "3", ".", ".", "5"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", ".", ".", ".", ".", ".", "2", ".", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "8"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    print(solution.isValidSudoku(board_test))
