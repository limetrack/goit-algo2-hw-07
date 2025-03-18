from collections import OrderedDict


class SplayNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class SplayTree:
    def __init__(self):
        self.root = None
        self.cache = OrderedDict()

    def _splay(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            if root.left is None:
                return root
            if key < root.left.key:
                root.left.left = self._splay(root.left.left, key)
                root = self._rotate_right(root)
            elif key > root.left.key:
                root.left.right = self._splay(root.left.right, key)
                if root.left.right is not None:
                    root.left = self._rotate_left(root.left)
            return root if root.left is None else self._rotate_right(root)
        else:
            if root.right is None:
                return root
            if key > root.right.key:
                root.right.right = self._splay(root.right.right, key)
                root = self._rotate_left(root)
            elif key < root.right.key:
                root.right.left = self._splay(root.right.left, key)
                if root.right.left is not None:
                    root.right = self._rotate_right(root.right)
            return root if root.right is None else self._rotate_left(root)

    def _rotate_right(self, node):
        left_child = node.left
        node.left = left_child.right
        left_child.right = node
        return left_child

    def _rotate_left(self, node):
        right_child = node.right
        node.right = right_child.left
        right_child.left = node
        return right_child

    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)
        self.cache[key] = value
        if len(self.cache) > 100:
            self.cache.popitem(last=False)

    def _insert(self, root, key, value):
        if root is None:
            return SplayNode(key, value)
        root = self._splay(root, key)
        if root.key == key:
            return root
        new_node = SplayNode(key, value)
        if key < root.key:
            new_node.right = root
            new_node.left = root.left
            root.left = None
        else:
            new_node.left = root
            new_node.right = root.right
            root.right = None
        return new_node

    def search(self, key):
        self.root = self._splay(self.root, key)
        if self.root and self.root.key == key:
            return self.root.value
        return None
