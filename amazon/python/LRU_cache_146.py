# Hashmap / Ordered dictionary to record visit order and fast visit
from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dict = OrderedDict()

    def get(self, key):
        if key not in self.dict:
            return -1
        val = self.dict[key]
        self.dict.move_to_end(key, last=True)
        return val

    def put(self, key, value):
        if key in self.dict:
            del self.dict[key]
        elif len(self.dict) == self.capacity:
            self.dict.popitem(last=False)
        self.dict[key] = value


# Note: or use common dict (O(1) get/delete)
# and linked list (memorize visit order)
class Node:
    def __init__(self, key, val):
        # Key and val need to both stored in the node
        # Otherwise unable to delete when full
        self.key = key
        self.val = val
        self.next = None
        self.pre = None


class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.capacity = capacity
        self.head.next = self.tail
        self.tail.pre = self.head
        self.dict = {}  # Key as key, node as value
        print(self.capacity)

    def delete_node(self, to_delete):
        to_delete.next.pre = to_delete.pre
        to_delete.pre.next = to_delete.next

    def add_node(self, add):
        self.tail.pre.next = add
        add.pre = self.tail.pre
        add.next = self.tail
        self.tail.pre = add

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        val = self.dict[key].val
        self.put(key, val)
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            node = self.dict[key]
            del self.dict[key]
            self.delete_node(node)
        elif len(self.dict) >= self.capacity:
            node = self.head.next
            del self.dict[node.key]
            self.delete_node(node)
        new_node = Node(key, value)
        self.add_node(new_node)
        self.dict[key] = new_node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
