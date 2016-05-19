"""
Binary Tree
A binary tree is a hierarchial data structure in which each node has at most
two children, which are referred to as the left child and the right child.
Insertion is O(1) and deletion is O(n).
Tree traversals are O(n).
Reference used: http://geeksquiz.com/binary-search-tree-set-2-delete/
and http://www.geeksforgeeks.org/write-a-c-program-to-delete-a-tree/
"""


class BTNode(object):
    """
    Class to create a Binary Tree Node, insert, delete child nodes and
    print inorder, preorder and postorder traversals.

    >>> from pydsa import binary_tree
    >>> bt = binary_tree.BTNode(1)
    >>> bt.insert("left", 2)
    >>> bt.insert("right", 3)
    >>> bt.inorder(bt)
    [2, 1, 3]
    >>> bt.preorder(bt)
    [1, 2, 3]
    >>> bt.postorder(bt)
    [2, 3, 1]
    >>> bt.delete(bt.left)
    >>> bt.inorder(bt)
    [1, 3]
    """
    def __init__(self, key, left=None, right=None):
        """
        Initializes a node with value key and optionally with left and/or
        right child nodes.
        """
        self.left = left
        self.right = right
        self.key = key
        self.inlist = []
        self.prelist = []
        self.postlist = []

    def insert(self, child, key):
        """
        Takes in a string child to insert the new node with value key at left
        or right of current node.
        """
        childNode = BTNode(key)
        if child == "left":
            self.left = childNode
        elif child == "right":
            self.right = childNode

    def delete(self, root):
        self.deleteUtil(self, root)

    def deleteUtil(self, node, root):
        """
        Recursively searches sub-trees to find root (the node to be deleted).
        When found, replaces it with the child node if other is None or the
        inorder successor (and recursively deletes it) if both child nodes
        are not None.
        """
        if node is None:
            return node

        node.left = self.deleteUtil(node.left, root)
        node.right = self.deleteUtil(node.right, root)

        if node == root:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # Get inorder successor of root
            temp = self.getLeftmost(root.right)
            root.key = temp.key

            # Recursively delete inorder successor
            root.right = self.deleteUtil(root.right, temp)

        return node

    def getLeftmost(self, root):
        """
        Returns the leftmost node in the tree rooted at root.
        """
        current = root
        while current.left is not None:
            current = current.left
        return current

    def inorder(self, root):
        self.inlist = []
        return self.inorderUtil(root)

    def inorderUtil(self, root):
        """
        Recursively traverses left sub-tree, then current node and then the
        right sub-tree.
        """
        if root:
            self.inorderUtil(root.left)
            self.inlist.append(root.key)
            self.inorderUtil(root.right)
        return self.inlist

    def preorder(self, root):
        self.prelist = []
        return self.preorderUtil(root)

    def preorderUtil(self, root):
        """
        Traverses the current node, then recursively traverses left sub-tree,
        and then the right sub-tree.
        """
        if root:
            self.prelist.append(root.key)
            self.preorderUtil(root.left)
            self.preorderUtil(root.right)
        return self.prelist

    def postorder(self, root):
        self.postlist = []
        return self.postorderUtil(root)

    def postorderUtil(self, root):
        """
        Recursively traverses left sub-tree, then the right sub-tree and then
        the current node.
        """
        if root:
            self.postorderUtil(root.left)
            self.postorderUtil(root.right)
            self.postlist.append(root.key)
        return self.postlist

    def boundaryTrav(self, root):
        """
        Boundary Traversal : print all the boundary nodes of the binary_tree
        """
        self.boundaryTrav_list = []
        return self.boundaryTrav_Util(root)

    def boundaryTrav_Util(self, root):
        """
        Print root node, boundary nodes of the left sub-tree, leaf nodes of left and 
        right sub-tree then boundary nodes of the right sub-tree.
        """
        if root:
            # root
            self.boundaryTrav_list.append(root.key)
            # left subtree boundary nodes
            self.boundaryLeft(root.left)
            # left subtree leaf nodes
            self.leavesNode(root.left)
            # right subtree leaf nodes
            self.leavesNode(root.right)
            # right subtree boundary nodes
            self.boundaryRight(root.right)
        return self.boundaryTrav_list

    def boundaryLeft(self, root):
        """
        Top-down left boundary nodes
        """
        if root:
            if root.left:
                self.boundaryTrav_list.append(root.key)
                self.boundaryLeft(root.left)
            elif root.right:
                self.boundaryTrav_list.append(root.key)
                self.boundaryLeft(root.right)

    def boundaryRight(self, root):
        """
        Bottom-up right boundary nodes
        """
        if root:
            if root.right:
                self.boundaryRight(root.right)
                self.boundaryTrav_list.append(root.key)
            elif root.left:
                self.boundaryRight(root.left)
                self.boundaryTrav_list.append(root.key)

    def leavesNode(self, root):
        """
        Leaf nodes
        """
        if root:
            self.leavesNode(root.left)

            if root.left is None and root.right is None:
                self.boundaryTrav_list.append(root.key)

            self.leavesNode(root.right)
