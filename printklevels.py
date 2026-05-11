class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printkdistance(root, k):
    if root is None:
        return
    if k == 0:
        print(root.data, end=' ')
    else:
        printkdistance(root.left, k-1)
        printkdistance(root.right, k-1)

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(8)

    k = 2
    print(f"Nodes at ditance {k} from root are: ")
    printkdistance(root, k)
    print()

if __name__ == "__main__":
    main()