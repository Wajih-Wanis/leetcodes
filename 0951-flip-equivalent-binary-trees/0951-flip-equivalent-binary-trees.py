# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def comparatif(head1,head2):
            if not head1 and head2:
                return False
            if not head2 and head1:
                return False
            if not head1 and not head2:
                return True
            
            if head1 and head2:
                if head1.val == head2.val:
                    return True and ((comparatif(head1.left,head2.right) and comparatif(head1.right,head2.left)) or (comparatif(head1.right,head2.right) and comparatif(head1.left,head2.left)))
                else:
                    return False
        
        return comparatif(root1,root2)

