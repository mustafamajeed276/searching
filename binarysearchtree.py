class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def newNode(item):
    temp = Node(item)
    temp.key = item
    temp.left = temp.right = None
    return temp

def insert(node, key):
    if node is None:
        return newNode(key)

    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)

    return node

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=' ')
        inorder(root.right)



if __name__ == "__main__":

    root = None

    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)

    inorder(root)