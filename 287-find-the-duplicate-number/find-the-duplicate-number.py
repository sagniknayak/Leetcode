class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        uniq = set()
        for elem in nums:
            if elem in uniq:
                return elem
            else:
                uniq.add(elem)


        