# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.is_there = dict()
        self.clean_tree(root, 0)

    def clean_tree(self, root, root_value):
        if root is None:
            return None
        root.value = root_value
        self.is_there[root_value] = True
        root.left = self.clean_tree(root.left, root_value*2+1)
        root.right = self.clean_tree(root.right, root_value*2+2)
        return root



    def find(self, target: int) -> bool:
        return self.is_there.get(target, False)


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)