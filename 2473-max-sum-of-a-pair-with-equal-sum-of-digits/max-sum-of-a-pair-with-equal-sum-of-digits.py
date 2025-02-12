class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        sums = dict()
        for num in nums:
            digsum = 0
            dupnum = num
            while dupnum!=0:
                digsum+=dupnum%10
                dupnum//=10
            sums[digsum] = sums.get(digsum,[])+[num]
        clean_sums = {k:v for k,v in sums.items() if len(v)>=2}
        if clean_sums:
            maxsum = 0
            for nums in clean_sums.values():
                nums.sort()
                if maxsum < nums[-1]+nums[-2]:
                    maxsum = nums[-1]+nums[-2]
            return maxsum
        else:
            return -1