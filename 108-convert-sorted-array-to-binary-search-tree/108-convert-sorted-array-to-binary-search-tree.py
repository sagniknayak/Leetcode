# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.taken = list()
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        for _ in nums:
            self.taken.append(False)
        numbers = list()
        for i in range(len(nums)):
            numbers.append((nums[i], i))
            
            
        def binarySearch(subset):
            if subset == []:
                return None
            mid = len(subset)//2
            if not self.taken[mid+subset[0][1]]:
                self.taken[mid+subset[0][1]] = True
                return TreeNode(subset[mid][0], binarySearch(subset[:mid]), binarySearch(subset[mid+1:]))
            else:
                return None
        
        return binarySearch(numbers)