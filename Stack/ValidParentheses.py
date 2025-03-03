"""
https://neetcode.io/problems/validate-parentheses
"""


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 or not s:
            return False

        stack = []
        parentheses = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in parentheses:
                if not stack or stack[-1] != parentheses[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)

        return not stack


if __name__ == "__main__":
    solution: Solution = Solution()
    print(solution.isValid("()"))
    print(solution.isValid("([{}])"))
    print(solution.isValid("[(])"))
