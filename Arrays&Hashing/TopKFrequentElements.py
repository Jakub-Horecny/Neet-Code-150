"""
https://neetcode.io/problems/top-k-elements-in-list
"""
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        result = []
        for i in sorted(count, key=count.get, reverse=True)[:k]:
            result.append(i)

        return result


if __name__ == '__main__':
    solution: Solution = Solution()
    print(solution.topKFrequent([1, 2, 2, 3, 3, 3], 2))
    print(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2))
    print(solution.topKFrequent([7, 7], 1))
