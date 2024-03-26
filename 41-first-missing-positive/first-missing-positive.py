class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seq = OrderedDict([(i,True) for i in range(1,len(nums)+2)])
        for key in nums:
            try:
                del seq[key]
            except:
                pass

        return next(iter(seq.keys()))