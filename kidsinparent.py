class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
def findnodesonechild(root, single_child_nodes=None):
    if single_child_nodes is None:
        single_child_nodes = []

    if not root:
        return single_child_nodes
    
    if (root.left and not root.right) or (root.right and not root.left):
        single_child_nodes.append(root)

    findnodesonechild(root.left, single_child_nodes)
    findnodesonechild(root.right, single_child_nodes)

    return single_child_nodes

def findpathsinrange(root, low, high, current_path=None, current_sum=0, valid_paths=None):

    if valid_paths is None:
        valid_paths = []

    if current_path is None:
        current_path = []

    if root is None:
        return valid_paths

    current_path.append(root.val)
    current_sum += root.val

    if root.left is None and root.right is None:
        if low <= current_sum <= high:
            valid_paths.append(list(current_path))

    else:
        findpathsinrange(root.left, low, high, current_path, current_sum, valid_paths)
        findpathsinrange(root.right, low, high, current_path, current_sum, valid_paths)

    current_path.pop()
    return valid_paths

def main():
    root  = Node(2)
    root.left = Node(3)
    root.right = Node(5)
    root.left.left = Node(7)
    root.right.left = Node(8)
    root.right.right = Node(6)

    single_child_nodes = findnodesonechild(root)

    if not single_child_nodes:
        print(-1)
    else:
        print("Nodes with exactly one child:")
        for node in single_child_nodes:
            print(node.val, end=' ')
        print()

    low = 14
    high = 21

    valid_paths = findpathsinrange(root, low, high)
    if valid_paths:
        print(f"Root-to-leaf paths with sums in the range [{low}, {high}]:")
        for path in valid_paths:
            print(" -> ".join(map(str, path)))
    else:
        print(f"No root-to-leaf paths with sums in the range [{low}, {high}].")


if __name__ == "__main__":
    main()