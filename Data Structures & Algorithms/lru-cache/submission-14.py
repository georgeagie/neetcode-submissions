class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = self.nxt = None

class LRUCache:

    def __init__(self, capacity: int):
        self.kv = {}
        self.capacity = capacity
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.nxt = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key in self.kv.keys():
            self.remove(self.kv[key])
            self.add(self.kv[key])
            return self.kv[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.kv.keys():
            self.remove(self.kv[key])
        self.kv[key] = Node(key, value)
        self.add(self.kv[key])
        if len(self.kv) > self.capacity:
            lru = self.left.nxt
            self.remove(lru)
            del self.kv[lru.key]
    
    def remove(self, node: Node):
        prev, nxt = node.prev, node.nxt
        prev.nxt, nxt.prev = nxt, prev
    
    def add(self, node):
        prev, nxt = self.right.prev, self.right
        prev.nxt = nxt.prev = node
        node.nxt, node.prev = nxt, prev
        



