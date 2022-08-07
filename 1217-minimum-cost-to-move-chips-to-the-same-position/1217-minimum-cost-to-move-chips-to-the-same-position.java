class Solution {
    public int minCostToMoveChips(int[] position) {
        int n = position.length;
        int odd = 0;
        for(int pos: position) {
            if(pos%2==1)
                odd++;
        }
        if(odd>n-odd)
            return n-odd;
        else
            return odd;
    }
}