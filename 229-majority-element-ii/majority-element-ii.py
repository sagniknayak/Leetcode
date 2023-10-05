class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = dict()
        for elem in nums:
            freq[elem] = freq.get(elem,0)+1
        maj = len(nums)/3
        return list(filter(lambda x: freq[x]>maj, freq))