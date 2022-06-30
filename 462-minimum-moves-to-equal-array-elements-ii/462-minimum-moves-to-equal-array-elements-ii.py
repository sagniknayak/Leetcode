class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        val = nums[len(nums)//2]
        moves = sum(list(map(lambda x: abs(x-val), nums)))
        return moves