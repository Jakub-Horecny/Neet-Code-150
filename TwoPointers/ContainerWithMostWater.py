"""
https://neetcode.io/problems/max-water-container
"""
from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        global_max: int = 0
        start: int = 0
        end: int = len(heights) - 1

        while start < end:
            local_max = min(heights[start], heights[end]) * (end - start)
            global_max = max(global_max, local_max)

            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1

        return global_max


if __name__ == "__main__":
    solution: Solution = Solution()
    print(solution.maxArea([1, 7, 2, 5, 4, 7, 3, 6]))
    print(solution.maxArea([2, 2, 2]))
