#分别按照二叉树先序，中序和后序打印所有的节点。
#https://www.nowcoder.com/practice/a9fec6c46a684ad5a3abd4e365a9d362?tpId=117&tqId=1008937&tab=answerKey
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
# 
# @param root TreeNode类 the root of binary tree
# @return int整型二维数组
#
class Solution:
    def threeOrders(self , root ):
        # write code here
        self.res=[[],[],[]]
        self.dfs(root)
        return self.res
    def dfs(self,root):
        if not root:return
        self.res[0].append(root.val)
        self.dfs(root.left)
        self.res[1].append(root.val)
        self.dfs(root.right)
        self.res[2].append(root.val)
        return 
