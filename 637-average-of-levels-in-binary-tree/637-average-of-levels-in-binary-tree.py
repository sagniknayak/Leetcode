# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        level = 0
        def traverse(root, level):
            global avg
            if level == 0:
                avg = dict()
            avg[level] = avg.get(level, []) + [root.val]
            if root.left is not None:
                traverse(root.left, level+1)
            if root.right is not None:
                traverse(root.right, level+1)
        
        
        traverse(root, 0)
        result = list()
        for i in range(max(list(avg.keys()))+1):
            result.append(sum(avg[i])/len(avg[i]))
        return result