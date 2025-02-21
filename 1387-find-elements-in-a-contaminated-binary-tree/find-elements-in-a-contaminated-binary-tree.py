# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.is_there = dict()
        leaves = {root}
        flag = True
        ctr = 0
        while(flag):
            flag = False
            new_leaves = list()
            for leaf in leaves:
                if leaf is not None:
                    leaf.val = ctr
                    self.is_there[ctr] = True
                    new_leaves.append(leaf.left)
                    new_leaves.append(leaf.right)
                    flag = True
                else:
                    new_leaves.append(None)
                    new_leaves.append(None)
                ctr+=1
            leaves = new_leaves
            self.root = root

    def find(self, target: int) -> bool:
        return self.is_there.get(target, False)


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)