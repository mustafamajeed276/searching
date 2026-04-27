class Node:
    def __init__(self, data):
        self.left_child = None
        self.data = data
        self.right_child = None

def find_recurseive_size(root):
    if root is None:
        return 0
    return find_recurseive_size(root.left_child) + find_recurseive_size(root.right_child)   

def find_iterative_size(root):
    if root is None:
        return 0

    count = 0
    stack = []
    stack.append(root)

    while stack:
        node = stack.pop()
        count += 1

        if node.left_child is not None:
            stack.append(node.left_child)
        if node.right_child is not None:
            stack.append(node.right_child)

    return count

root = Node(1)
root.left_child = Node(2)
root.right_child = Node(3)
root.left_child.left_child = Node(4)
root.left_child.right_child = Node(5)
root.right_child.left_child = Node(6)
root.right_child.right_child = Node(7)
root.right_child.left_child.left_child = Node(8)
root.right_child.left_child.right_child = Node(9)


size_recursive = find_recurseive_size(root)
print(f"Size of the binary tree (recursive): {size_recursive}")

size_iterative = find_iterative_size(root)
print(f"Size of the binary tree (iterative): {size_iterative}")