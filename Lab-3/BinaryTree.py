class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if node is None:
            return TreeNode(value)
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        return node

    def __iter__(self):
        return self._inorder_generator(self.root)

    def _inorder_generator(self, node):
        if node:
            yield from self._inorder_generator(node.left)
            yield node.value
            yield from self._inorder_generator(node.right)


if __name__ == "__main__":
    bst = BinarySearchTree()
    elements = [5, 3, 7, 2, 4, 6, 9]

    for element in elements:
        bst.insert(element)

    for value in bst:
        print(value)
