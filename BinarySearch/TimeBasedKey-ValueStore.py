"""
https://neetcode.io/problems/time-based-key-value-store
"""


class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = []
        self.time_map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        ans, val = "", self.time_map.get(key, [])

        l, r = 0, len(val) - 1
        while l <= r:
            mid = (l + r) // 2
            if val[mid][1] <= timestamp:
                ans = val[mid][0]
                l = mid + 1
            else:
                r = mid - 1

        return ans


if __name__ == "__main__":
    pass
