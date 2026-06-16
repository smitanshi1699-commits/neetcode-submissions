# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def heightofTree(node) -> int:
            if node is None:
                return 0
            L = heightofTree(node.left)
            R = heightofTree(node.right)
            self.diameter = max(self.diameter , L + R)
            return 1 + max(L, R)
        heightofTree(root)
        return self.diameter