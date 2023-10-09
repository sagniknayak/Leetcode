class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        flag1 = False
        flag2 = False
        lp = 0
        rp = len(nums) - 1
        while not (flag1 and flag2) and lp<=rp:
            if nums[lp] != target:
                lp += 1
            else:
                flag1 = True
            
            if nums[rp] != target:
                rp -= 1
            else:
                flag2 = True
        return [lp, rp] if flag1 and flag2 else [-1,-1]