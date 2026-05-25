class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def haspathsum(node, target_sum):

    if node is None:
        return False

    remaining_sum = target_sum - node.data

    if remaining_sum == 0 and node.left is None and node.right is None:
        return True
    
    return haspathsum(node.left, remaining_sum) or haspathsum(node.right, remaining_sum)

def findpathsinmain(node, low, high, current_path=None, current_sum=0, valid_paths=None):

    if valid_paths is None:
        valid_paths = []

    if current_path is None:
        current_path = []

    if node is None:
        return valid_paths

    current_path.append(node.data)
    current_sum += node.data

    if node.left is None and node.right is None:
        if low <= current_sum <= high:
            valid_paths.append(list(current_path))
        else:
            findpathsinmain(node.left, low, high, current_path, current_sum, valid_paths)

        current_path.pop()

        return valid_paths

def main():
    target_sum = 21

    root = Node(10)
    root.left = Node(8)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(5)
    root.right.left = Node(2)         