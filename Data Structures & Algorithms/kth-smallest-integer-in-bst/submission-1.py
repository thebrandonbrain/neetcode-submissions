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
            add_to_list(lis, root.left)
            lis.append(root.val)
            add_to_list(lis, root.right)
        add_to_list(lis, root)
        return lis[k-1]