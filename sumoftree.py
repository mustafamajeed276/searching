class newNode:
    def __init__(self, data):
        self.val = data
        self.left = self.right = None

def transverse(root, tilt):
    if (not root):
        return 0

    left = transverse(root.left, tilt)
    right = transverse(root.right, tilt)

    tilt[0] += abs(left - right)

    return left + right + root.val

def Tilt(root):
    tilt = [0]
    transverse(root, tilt)
    return tilt[0]

if __name__ == "__main__":
    root = None
    root = newNode(4)
    root.left = newNode(2)
    root.right = newNode(9)
    root.left.left = newNode(3)
    root.left.right = newNode(8)
    root.right.right = newNode(7)
    print("Tilt of the given tree is", Tilt(root))        