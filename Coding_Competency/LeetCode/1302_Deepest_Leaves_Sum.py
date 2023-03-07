# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root) -> int:
        rootl = root
        rootr = root
        ret = 0
        while (rootl.left or rootl.right):
            if rootl.left:
                rootl = rootl.left
            else:
                rootl = rootl.right
        ret += rootl.val
        while (rootr.right or rootr.left):
            if rootr.right:
                rootr = rootr.right
            else:
                rootr = rootr.left
        ret += rootr.val
        return ret


# [1,2,3,4,5,null,6,7,null,null,null,null,8]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
root.left.left.left = TreeNode(7)
root.right.right.right = TreeNode(8)
print(Solution().deepestLeavesSum(root))
