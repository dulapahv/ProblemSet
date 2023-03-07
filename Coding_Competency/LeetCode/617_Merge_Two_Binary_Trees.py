from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        root = TreeNode()
        while root1.left or root1.right or root2.left or root2.right:
            root.val = root1.val + root2.val
            root1.val = root1.left
            root2.val = root2.left
        return root
            

tree1 = TreeNode(1, TreeNode(3, TreeNode(5, None, None), None), TreeNode(2, None, None))
tree2 = TreeNode(2, TreeNode(1, None, TreeNode(4, None, None)), TreeNode(3, None, TreeNode(7, None, None)))
print(Solution().mergeTrees(tree1, tree2))
