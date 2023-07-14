class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        subseq = dict()
        maxim = 0
        for elem in arr:
            val = subseq.get(elem-difference, 0) + 1
            subseq[elem] = val
            if maxim < val:
                maxim = val
        return maxim