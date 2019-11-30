from queue import LifoQueue as Stack

"""
Class definition for the nodes of the binary Tree.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Finds the lowest common ancestor of the given nodes in the tree.
    :param root: The root of the tree.
    :param p: TreeNode whose lowest common ancestor with q is to be found.
    :param q: TreeNode whose lowest common ancestor with p is to be found.
    :return: The lowest common ancestor of p and q if there is one.
    """

    # We use a stack to traverse the tree.
    stack = Stack()
    stack.put(root)

    # Dictionary to track the parents of each node.
    parents = {root: None}

    # We keep populating the parents dictionary till we haven't seen both
    # p and q.
    while p not in parents or q not in parents:

        # Get the node to be visited from the stack.
        node = stack.get()

        # Update the nodes children's parent and populate the stack
        if node.left:
            parents[node.left] = node
            stack.put(node.left)
        if node.right:
            parents[node.right] = node
            stack.put(node.right)

    # Set to hold unique ancestors as we traverse back along the parents
    # dictionary.
    ancestors = set()

    # Traverse upwards from p to the root of the tree and saving the path of
    # ancestors traversed along.
    while p:
        ancestors.add(p)
        p = parents[p]

    # Traverse upwards from q till we dont find a common ancestor in the path.
    while q not in ancestors:
        ancestors.add(q)
        q = parents[q]

    # return q if found else, q would be None.
    return q
