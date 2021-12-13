class Tree(object):
    def __init__(self, val, left=None, right=None):
        assert type(val) == int
        assert left == None or type(left) == Tree
        assert right == None or type(right) == Tree
        self.val = val
        self.left = left
        self.right = right


def sumTree(tree):
    summ = 0
    if tree is None:
        return 0
    if tree.left is None and tree.right is None:
        return tree.val
    if tree.left is not None:
        summ += sumTree(tree.left)
    if tree.right is not None:
        summ += sumTree(tree.right)

    summ += tree.val
    return summ


assert sumTree(None) == 0
assert sumTree(Tree(1)) == 1
assert sumTree(Tree(1, Tree(2))) == 3
assert sumTree(Tree(5, Tree(-1), Tree(-2))) == 2
assert sumTree(Tree(1, Tree(2, Tree(3, Tree(4))))) == 10
