class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        val = nums[len(nums)//2]
        moves = 0
        for item in nums:
            moves += abs(item-val)
        return moves