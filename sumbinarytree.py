class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def sum_recursive_tree(root):
    if root is None:
        return 0
    return sum_recursive_tree(root.left) + sum_recursive_tree(root.right) + root.key

if __name__ == '__main__':
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    root.left.right = Node(50)
    root.right.left = Node(60)
    root.right.right = Node(70)
    root.right.left.right = Node(80)

    total_sum = sum_recursive_tree(root)
    print(f"The sum of all nodes in the binary tree is: {total_sum}")