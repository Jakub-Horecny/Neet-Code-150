from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result: dict = {}
        for s in strs:
            ss: str = ''.join(sorted(s))
            if result.get(ss) is None:
                result[ss] = [s]
            else:
                result[ss].append(s)

        return list(result.values())


if __name__ == '__main__':
    solution: Solution = Solution()
    print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(solution.groupAnagrams(["X"]))
    print(solution.groupAnagrams([""]))

