"""
https://neetcode.io/problems/search-2d-matrix
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)  # rows
        n = len(matrix[0])  # columns

        start, end = 0, n * m - 1

        while start <= end:
            index = start + ((end - start) // 2)

            if matrix[int(index / n)][index % n] == target:
                return True
            elif matrix[int(index / n)][index % n] > target:
                end = index - 1
            else:
                start = index + 1

        return False


if __name__ == '__main__':
    solution: Solution = Solution()
    #print(solution.searchMatrix([[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], 10))
    print(solution.searchMatrix([[1], [3]], 2))
