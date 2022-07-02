class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        h_cuts = [0]+horizontalCuts+[h]
        v_cuts = [0]+verticalCuts+[w]
        return int((max([h_cuts[i]-h_cuts[i-1] for i in range(len(h_cuts))])*max([v_cuts[i]-v_cuts[i-1] for i in range(len(v_cuts))]))%(1000000007))
        