"""
https://neetcode.io/problems/longest-consecutive-sequence
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        next_index = 1
        local_max = 1
        global_max = 1

        for num in nums:
            if next_index == len(nums):
                return max(local_max, global_max)

            if num == nums[next_index]:
                next_index += 1
                continue

            if num + 1 != nums[next_index]:
                global_max = max(global_max, local_max)
                local_max = 1
            elif num + 1 == nums[next_index]:
                local_max += 1
            next_index += 1

        return max(global_max, local_max)


if __name__ == '__main__':
    solution: Solution = Solution()
    print(solution.longestConsecutive([2, 20, 4, 10, 3, 4, 5]))
    print(solution.longestConsecutive([0, 3, 2, 5, 4, 6, 1, 1]))
    print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))

