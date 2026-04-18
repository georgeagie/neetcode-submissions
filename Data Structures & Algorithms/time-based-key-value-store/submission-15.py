class TimeMap:

    def __init__(self):
        self.key_value = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_value[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if (key not in self.key_value.keys()):
            return ""
        elif (timestamp > self.key_value[key][-1][1]):
            return self.key_value[key][-1][0]

        # run bs
        return self.search(self.key_value[key], timestamp)

    def search(self, values, timestamp):
        closest_str = ""
        l = 0
        r = len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            if values[mid][1] == timestamp:
                return values[mid][0]
            elif values[mid][1] < timestamp:
                l = mid + 1
                closest_str = values[mid][0]
            else:
                r = mid - 1
        
        return closest_str

