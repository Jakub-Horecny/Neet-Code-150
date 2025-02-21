"""
https://neetcode.io/problems/three-integer-sum
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result: list = []
        nums.sort()

        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            start: int = i + 1
            end: int = len(nums) - 1

            while start < end:
                if nums[i] + nums[start] + nums[end] == 0:
                    result.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1

                elif nums[i] + nums[start] + nums[end] < 0:
                    start += 1
                else:
                    end -= 1

        return result


if __name__ == "__main__":
    solution: Solution = Solution()
    print(solution.threeSum([0, 0, 0, 0]))
    print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
    print(solution.threeSum([0, 1, 0]))
