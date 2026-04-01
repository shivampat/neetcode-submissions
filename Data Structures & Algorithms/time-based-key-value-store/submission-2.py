from collections import defaultdict

class TimeMap:
    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        keylist = self.data[key]
        # O(n) solution
        # for i in range(len(keylist)-1, -1, -1):
        #     if keylist[i][1] <= timestamp:
        #         return keylist[i][0]

        # O(logn) solution
        # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        l, r = 0, len(keylist)-1
        result = None
        while l <= r:
            m = l + ((r-l) // 2)

            if keylist[m][1] <= timestamp:
                result = keylist[m][0]
                l = m + 1
            else:
                r = m - 1
        
        if result:
            return result
        
        return ""

            
        
