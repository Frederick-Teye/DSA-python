class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            _insert(data, self.root)

    def _insert(self, data, current_node):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                _insert(data, current_node.left)
        elif data > current_node.data:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                _insert(data, current_node.right)
        else:
            print(f"{data} already exists in the tree!")

    def in_order_traversal(self):
        if self.root is not None:
            _in_order_traversal(self.root)

    def _in_order_traversal(self, current_node):
        if current_node is not None:
            _in_order_traversal(current_node.left)
            print(f"{current_node.data}", end=" ")
            _in_order_traversal(current_node.right)

    def pre_order_traversal(self):
        if self.root is not None:
            _pre_order_traversal(self.root)

    def _pre_order_traversal(self, current_node):
        if current_node is not None:
            print(f"{current_node.data}", end=" ")
            _pre_order_traversal(current_node.left)
            _pre_order_traversal(current_node.right)