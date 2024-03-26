class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seq = OrderedDict([(i, True) for i in nums])
        for check in range(1,len(nums)+2):
            if seq.get(check, False):
                pass
            else:
                return check
    
        
        