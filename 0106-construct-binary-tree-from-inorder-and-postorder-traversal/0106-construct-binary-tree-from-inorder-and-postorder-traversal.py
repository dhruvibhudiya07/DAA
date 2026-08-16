# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        if not inorder:
            return None
        root_value = postorder.pop()
        root = TreeNode(root_value)
        index = inorder.index(root_value)
        root.right = self.buildTree(inorder[index + 1:], postorder)
        root.left = self.buildTree(inorder[:index], postorder)
        return root

        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        