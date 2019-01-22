# Hashmap / Ordered dictionary to record visit order and fast visit


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dict = collections.OrderedDict()

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
