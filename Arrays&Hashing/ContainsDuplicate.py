"""
https://neetcode.io/problems/duplicate-integer
"""
from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return True if len(nums) != len(set(nums)) else False


if __name__ == '__main__':
    solution: Solution = Solution()

    nums_test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(solution.hasDuplicate(nums_test))
    nums_test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    print(solution.hasDuplicate(nums_test))
    nums_test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]
    print(solution.hasDuplicate(nums_test))
    nums_test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2]
    print(solution.hasDuplicate(nums_test))
    nums_test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
    print(solution.hasDuplicate(nums_test))
    nums_test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4]
    print(solution.hasDuplicate(nums_test))
    nums_test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]
    print(solution.hasDuplicate(nums_test))
    nums_test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6]
    print(solution.hasDuplicate(nums_test))
    nums_test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
    print(solution.hasDuplicate(nums_test))
    nums_test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2]
