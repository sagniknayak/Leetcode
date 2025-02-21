# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        leaves = {root}
        flag = True
        ctr = 0
        while(flag):
            flag = False
            new_leaves = list()
            for leaf in leaves:
                if leaf is not None:
                    leaf.val = ctr
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
        det_path = ""
        dup = target
        while(dup>0):
            if dup%2 == 0:
                det_path = "R"+det_path
                dup = (dup-2)//2
            else:
                det_path = "L"+det_path
                dup = (dup-1)//2
        found = True
        current = self.root
        for move in det_path:
            if move == 'L':
                current = current.left
            else:
                current = current.right
            if current is None:
                found = False
                break

        return found


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)