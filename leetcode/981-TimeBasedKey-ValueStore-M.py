class TimeMap:

    def __init__(self):
        self.time_based_key_value = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_based_key_value:
            self.time_based_key_value[key] = []
        self.time_based_key_value[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_based_key_value:
            return ""
        else:
            left, right = 0, len(self.time_based_key_value[key]) - 1
            vals = self.time_based_key_value.get(key, [])
            res = ""

            while left <= right:
                mid = (left + right) // 2
                if vals[mid][1] <= timestamp:
                    res = vals[mid][0]
                    left = mid + 1
                else:
                    right = mid - 1
            return res 


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# ["TimeMap", "set", "get", "get", "set", "get", "get"]
# [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
print("Time Complexity is O(log n)")