from collections import defaultdict

class TimeMap:
    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        keylist = self.data[key]
        # O(n) solution
        for i in range(len(keylist)-1, -1, -1):
            if keylist[i][1] <= timestamp:
                return keylist[i][0]
        
        return ""

            
        
