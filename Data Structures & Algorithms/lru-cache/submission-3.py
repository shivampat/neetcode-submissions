class ListNode:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.lru = ListNode()
        self.mru = ListNode()

        self.lru.next, self.mru.prev = self.mru, self.lru
    
    def _removeNode(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
    
    def _addMRUNode(self, node):
        prev = self.mru.prev
        prev.next = node
        node.prev = prev
        node.next = self.mru
        self.mru.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self._removeNode(self.cache[key])
            self._addMRUNode(self.cache[key])
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._removeNode(self.cache[key])
        
        newNode = ListNode(key=key, val=value)
        self._addMRUNode(newNode)
        self.cache[key] = newNode

        if len(self.cache) > self.capacity:
            lruNode = self.lru.next
            lruNodeKey = lruNode.key
            self._removeNode(lruNode)
            del self.cache[lruNodeKey]