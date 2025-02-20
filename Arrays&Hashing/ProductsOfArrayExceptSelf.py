"""
https://neetcode.io/problems/products-of-array-discluding-self
"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]

        for i in range(len(nums)-2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i+1]

        result = [pre * pos for pre, pos in zip(prefix, postfix)]
        return result


if __name__ == '__main__':
    solution: Solution = Solution()
    print(solution.productExceptSelf([2, 2, 3, 4]))
    print(solution.productExceptSelf([1, 2, 3, 4, 5]))
    print(solution.productExceptSelf([-1, 0, 1, 2, 3]))
