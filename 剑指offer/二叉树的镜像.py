#操作给定的二叉树，将其变换为源二叉树的镜像。
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
# 
# @param pRoot TreeNode类 
# @return void
#
class Solution:
    def Mirror(self , pRoot ):
        # write code here
        if not pRoot:
            return pRoot
        node=pRoot.left
        pRoot.left=pRoot.right
        pRoot.right=node
        self.Mirror(pRoot.left)
        self.Mirror(pRoot.right)
        return pRoot
