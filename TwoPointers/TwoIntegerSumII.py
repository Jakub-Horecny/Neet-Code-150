"""
https://neetcode.io/problems/two-integer-sum-ii
"""
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start: int = 0
        end: int = len(numbers) - 1

        while start < end:
            if numbers[start] + numbers[end] == target:
                return [start + 1, end + 1]
            elif numbers[start] + numbers[end] > target:
                end -= 1
            elif numbers[start] + numbers[end] < target:
                start += 1

        return []


if __name__ == '__main__':
    solution: Solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))
    print(solution.twoSum([1, 2, 3, 4], 9))
    print(solution.twoSum([1, 2, 3, 4], 3))
