class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
        return root
    
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)

if __name__ == "__main__":
    r = Node(1.5)
    r = insert(r, 1)
    r = insert(r, 2)
    r = insert(r, 3)
    r = insert(r, 4)
    r = insert(r, 5)
    r = insert(r, 6)

    inorder(r)        