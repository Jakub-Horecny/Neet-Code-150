"""
https://neetcode.io/problems/find-minimum-in-rotated-sorted-array
"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        ans: int = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                ans = min(nums[l], ans)

            mid = (l + r) // 2

            ans = min(nums[mid], ans)

            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid

        return ans


if __name__ == "__main__":
    solution: Solution = Solution()
    print(solution.findMin([2, 1]))
    print(solution.findMin([4, 5, 6, 7]))
    print(solution.findMin([3, 4, 5, 6, 1, 2]))
