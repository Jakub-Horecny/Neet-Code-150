"""
https://neetcode.io/problems/permutation-string
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        substring: dict = {}
        for i in s1:
            substring[i] = 1 + substring.get(i, 0)

        s2_subs: dict = {}
        for i in s2[:len(s1)]:
            s2_subs[i] = 1 + s2_subs.get(i, 0)

        l_index = 0

        for s in s2[len(s1):]:
            if s2_subs == substring:
                return True
            else:
                if s2_subs[s2[l_index]] == 1:
                    del s2_subs[s2[l_index]]
                else:
                    s2_subs[s2[l_index]] -= 1
                    
                s2_subs[s] = 1 + s2_subs.get(s, 0)
                l_index += 1

        return s2_subs == substring


if __name__ == "__main__":
    solution: Solution = Solution()

    print(solution.checkInclusion("adc", "dcda"))
    print(solution.checkInclusion("abc", "lecabee"))
    print(solution.checkInclusion("abc", "lecaabee"))
    print(solution.checkInclusion("trinitrophenylmethylnitramine",
                                  "dinitrophenylhydrazinetrinitrophenylmethylnitramine"))

