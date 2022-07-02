class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        h_cuts = [0]+horizontalCuts+[h]
        v_cuts = [0]+verticalCuts+[w]
        max_h = 0
        for i in range(len(h_cuts)):
            h_val = h_cuts[i]-h_cuts[i-1]
            if h_val > max_h:
                max_h = h_val
        max_v = 0
        for i in range(len(v_cuts)):
            v_val = v_cuts[i]-v_cuts[i-1]
            if v_val > max_v:
                max_v = v_val
                
        print(f'max h {max_h}  max v {max_v}')
        print(f'val {max_h*max_v}')
                
        return int((max_h*max_v) % (1000000007))