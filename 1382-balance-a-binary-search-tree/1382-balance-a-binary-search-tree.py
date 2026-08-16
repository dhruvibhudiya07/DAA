# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def balanceBST(self, root):
        values = []
        def inorder(node):
            if node:
                inorder(node.left)
                values.append(node.val)
                inorder(node.right)
        inorder(root)
        def build(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(values[mid])
            node.left = build(left, mid - 1)
            node.right = build(mid + 1, right)
            return node
        return build(0, len(values) - 1)
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        