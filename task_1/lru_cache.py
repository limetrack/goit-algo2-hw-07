from doubly_linked_list import DoublyLinkedList


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.list = DoublyLinkedList()

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.list.move_to_front(node)
            return node.data[1]
        return None

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.data = (key, value)
            self.list.move_to_front(node)
        else:
            if len(self.cache) >= self.capacity:
                last = self.list.remove_last()
                if last:
                    del self.cache[last.data[0]]
            new_node = self.list.push(key, value)
            self.cache[key] = new_node

    def invalidate(self, index):
        """Видалення всіх записів, які містять змінений індекс"""
        keys_to_delete = [key for key in list(self.cache.keys()) if key[0] <= index <= key[1]]
        for key in keys_to_delete:
            node = self.cache.pop(key)
            self.list.remove(node)
