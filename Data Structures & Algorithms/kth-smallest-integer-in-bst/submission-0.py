# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        lis = []
        def add_to_list(lis, root):    
            if not root:
                return
            else:
                lis.append(root.val)
            add_to_list(lis, root.left)
            add_to_list(lis, root.right)
        add_to_list(lis, root)
        lis.sort()
        for index, i in enumerate(lis):
            if index == k - 1:
                return i