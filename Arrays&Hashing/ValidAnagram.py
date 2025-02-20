"""
https://neetcode.io/problems/is-anagram
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count: dict = {}
        t_count: dict = {}

        for ss, tt in zip(s, t):
            s_count[ss] = 1 + s_count.get(ss, 0)
            t_count[tt] = 1 + t_count.get(tt, 0)
        return s_count == t_count


if __name__ == '__main__':
    solution: Solution = Solution()
    print(solution.isAnagram("racecar", "carrace"))
"""    print(solution.isAnagram("rat", "car"))
    print(solution.isAnagram("a", "ab"))
    print(solution.isAnagram("ab", "a"))
    print(solution.isAnagram("ab", "ba"))
    print(solution.isAnagram("ba", "ab"))"""