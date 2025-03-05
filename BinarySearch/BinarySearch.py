"""
https://neetcode.io/problems/binary-search
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        start, end = 0, len(nums) - 1

        while start <= end:
            index = start + ((end - start) // 2)

            if nums[index] == target:
                return index
            elif nums[index] > target:
                end = index - 1
            else:
                start = index + 1

        return -1


if __name__ == '__main__':
    solution: Solution = Solution()
    print(solution.search([-1, 0, 2, 4, 6, 8], 4))
    print(solution.search([-1, 0, 2, 4, 6, 8], 3))
    print(solution.search([2, 5], 5))
