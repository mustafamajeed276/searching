class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printkdistance(root, k):

    if root is None or k < 0:
        return
    
    if k == 0:
        print(root.data, end=' ')
        return
    
    printkdistance(root.left, k-1)
    printkdistance(root.right, k-1)

def printkdistancenode(root, target, k):
    if root is None:
        return -1

    if root == target:
        print(f"Nodes at distance {k} from target node {target.data} are: ")
        printkdistance(root, k)
        return 0
    
    dl = printkdistancenode(root.left, target, k)

    if dl != -1:
        if dl + 1 == k:
            print(root.data, end=' ')
        else:
            printkdistance(root.right, k-dl-2)

        return 1 + dl

    dr = printkdistancenode(root.right, target, k)

    if dr != -1:
        if dr + 1 == k:
            print(root.data, end=' ')
        else:
            printkdistance(root.left, k-dr-2)

        return 1 + dr
    
    return -1

def main():
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)

    target = root.left.right
    k = 2

    printkdistancenode(root, target, k)
    print()

if __name__ == "__main__":
    main()