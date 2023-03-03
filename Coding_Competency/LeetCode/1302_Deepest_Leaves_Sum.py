# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root) -> int:
        q = [root]
        while q:
            pre = q
            current = []
            for p in q:
                for child in [p.left, p.right]:
                    if child:
                        current.append(child)
            q = current
        return sum(node.val for node in pre)


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
