"""
https://neetcode.io/problems/longest-substring-without-duplicates
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest: dict = {}
        length: int = 0
        res: int = 0

        for i, let in enumerate(s):
            if let in longest:
                length = max(longest[let] + 1, length)
            longest[let] = i
            res = max(res, i - length + 1)

        return res


if __name__ == "__main__":
    solution: Solution = Solution()
    print(solution.lengthOfLongestSubstring("aabc"))
    print(solution.lengthOfLongestSubstring("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcdefghijk"))
    print(solution.lengthOfLongestSubstring("thequickbrownfoxjumpsoverthelazydogthequickbrownfoxjumpsovert"))
    print(solution.lengthOfLongestSubstring("dvdf"))
    print(solution.lengthOfLongestSubstring("zxyzxyz"))
    print(solution.lengthOfLongestSubstring("xxxx"))
