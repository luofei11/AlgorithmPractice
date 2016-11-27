class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def recoverBST(root):
    info = [None, None, None]
    def inorderHelper(node):
        if not node:
            return
        inorderHelper(node.left)
        if info[0]:
            if node.val <= info[0].val:
                if not info[1]:
                    info[1] = info[0]
                    info[2] = node
                else:
                    info[2] = node
        info[0] = node
        inorderHelper(node.right)

    inorderHelper(root)
    #swap the wrong nodes' val
    info[1].val, info[2].val = info[2].val, info[1].val


def printTree(node):
    if not node:
        return
    print node.val
    printTree(node.left)
    printTree(node.right)

root = TreeNode(10)
root.left = TreeNode(8)
root.right = TreeNode(12)
root.left.left = TreeNode(9)
root.left.right = TreeNode(7)

printTree(root)
recoverBST(root)
printTree(root)


