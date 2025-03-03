"""
https://neetcode.io/problems/evaluate-reverse-polish-notation
"""
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token.startswith("-") and token[1:].isdigit() or token.isdigit():
                stack.append(int(token))
            else:
                temp1 = stack.pop()
                temp2 = stack.pop()
                if token == '*':
                    stack.append(temp2 * temp1)
                elif token == '+':
                    stack.append(temp2 + temp1)
                elif token == '-':
                    stack.append(temp2 - temp1)
                elif token == '/':
                    stack.append(int(temp2 / temp1))

        return stack.pop()


if __name__ == '__main__':
    solution: Solution = Solution()
    print(solution.evalRPN(["1", "2", "+", "3", "*", "4", "-"]))
    print(solution.evalRPN(["2", "1", "+", "3", "*"]))
