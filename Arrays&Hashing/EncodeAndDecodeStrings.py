"""
https://neetcode.io/problems/string-encode-and-decode
"""
from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += s + "&#"
        return res

    def decode(self, s: str) -> List[str]:
        result = []

        start = 0
        for i, symbol in enumerate(s):
            if symbol == "&":
                if i + 1 < len(s) and s[i + 1] == '#':
                    result.append(s[start:i])
                    start = i + 2

        return result


if __name__ == '__main__':
    solution: Solution = Solution()
    code = (solution.encode(["neet", "code", "love", "you"]))
    print(code)
    print(solution.decode(code))

    code = (solution.encode(["we", "say", ":", "yes", "!@#$%^&*()"]))
    print(code)
    print(solution.decode(code))
