"""
https://neetcode.io/problems/two-integer-sum
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums_dict: dict = {}
        for index, num in enumerate(nums):
            if target - num in nums_dict:
                return [nums_dict[target - num], index]
            nums_dict[num] = index
        return []


if __name__ == '__main__':
    solution: Solution = Solution()

    nums_test = [2, 7, 11, 15]
    target_test = 9
    print(solution.twoSum(nums_test, target_test))

    nums_test = [3, 2, 4]
    target_test = 6
    print(solution.twoSum(nums_test, target_test))

    nums_test = [3, 3]
    target_test = 6
    print(solution.twoSum(nums_test, target_test))

    nums_test = [3, 2, 3]
    target_test = 6
    print(solution.twoSum(nums_test, target_test))
