class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

def insert(root, new_value):
    if root is None:
        return BinaryTreeNode(new_value)
    if new_value < root.data:
        root.left_child = insert(root.left_child, new_value)
    elif new_value > root.data:
        root.right_child = insert(root.right_child, new_value)
    else:
        print(f"Value {new_value} already exists in the tree.")
    return root

def delete_tree(root):
    if root:
        delete_tree(root.left_child)
        root.left_child = None
        delete_tree(root.right_child)
        root.right_child = None
        print(f"Deleted node with value: {root.data}")
        root.data = None


root = insert(None, 15)
insert(root, 10)
insert(root, 25)
insert(root, 6)
insert(root, 14)
insert(root, 20)
insert(root, 60)

print("Deleting the tree...")
delete_tree(root)
root = None