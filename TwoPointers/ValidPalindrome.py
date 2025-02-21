"""
https://neetcode.io/problems/is-palindrome
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        start: int = 0
        end: int = len(s) - 1

        while start < end:
            if s[start] == " " or not s[start].isalnum():
                start += 1
                continue
            elif s[end] == " " or not s[end].isalnum():
                end -= 1
                continue
            elif s[start].lower() == s[end].lower():
                start += 1
                end -= 1
            else:
                return False

        return True


if __name__ == '__main__':
    solution: Solution = Solution()
    print(solution.isPalindrome("Was it a car or a cat I saw?"))
    print(solution.isPalindrome("tab a cat"))
