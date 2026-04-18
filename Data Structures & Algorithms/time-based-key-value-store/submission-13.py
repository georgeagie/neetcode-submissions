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
        res = ""
        l = 0
        r = len(values) - 1
        
        while l <= r:
            mid = (l + r) // 2
            # If we find the exact timestamp, return it immediately
            if values[mid][1] == timestamp:
                return values[mid][0]
            
            # If mid timestamp is less than target, it's a candidate!
            # Save it and look to the right for a closer (larger) timestamp.
            if values[mid][1] < timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                # If mid timestamp is too big, look to the left.
                r = mid - 1
                
        return res
