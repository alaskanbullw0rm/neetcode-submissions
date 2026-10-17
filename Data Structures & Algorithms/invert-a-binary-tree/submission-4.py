# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if (root is None):
            return None
        #Child node
        elif (root.left is None and root.right is None):
            print ("No Children")
            return root
        #Left child
        elif (root.left is None):
            print ("No left child")
            nodeRight = root.right
            root.left = nodeRight
            root.right = None
            self.invertTree(root.left)
        #No Right child
        elif (root.right is None):
            print("No right child")
            nodeLeft = root.left
            root.right = nodeLeft
            root.left = None
            self.invertTree(root.right)
        else:
            print("rotating both")
            nodeLeft = root.left
            root.left = root.right
            root.right = nodeLeft
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root
        