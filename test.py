from binary_tree import BinaryTree as BT

bn_tree = BT()
data = [8, 10, 3, 14, 6, 13, 7, 4, 1]

for element in data:
    bn_tree.insert(element)

print("Pre-order traversal:", end=" ")
bn_tree.pre_order_traversal()

print("\n\nIn-order traversal:", end=" ")
bn_tree.in_order_traversal()

print("\n\nPost-order traversal:", end=" ")
bn_tree.post_order_traversal()

print("\n\nLevel-order traversal:", end=" ")
bn_tree.level_order_traversal()

print(
    "\n\n\nAnother way of implementing in-order traversal\n"
    + "--------------------------------------------\n"
)


def print_inorder(root):
    if root:
        # first recur on left child
        print_inorder(root.left)
        # then print the data of node
        print(root.data, end=" ")
        # now recur on right child
        print_inorder(root.right)


# The function above can be used to print out traversing a binary tree
# in-orderly when the root node is passed to it as an argument.
# pre-order and post order can also be handled this way outside a brinary
# search tree class.


print_inorder(bn_tree.root)
print("\n")
