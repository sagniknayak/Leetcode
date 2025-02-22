# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        base = TreeNode()
        traversal += '-'
        value = ""
        level = 0
        last_root = {-1: base}
        for char in traversal:
            if char == "-":
                if value is not "":
                    newNode = TreeNode(int(value))
                    parent = last_root[level - 1]
                    if parent.left is not None:
                        parent.right = newNode
                    else:
                        parent.left = newNode
                    last_root[level] = newNode
                    value = ""
                    level = 0
                level += 1
            else:
                value += char

        return base.left