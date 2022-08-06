class Solution {
    public int[] sumZero(int n) {
        int[] nUniq = new int[n];
        int half = n/2;
        int fill = half;
        for(int i=0; i<half; i++) {
            nUniq[i] = -fill;
            nUniq[n-1-i] = fill;
            fill--;
        }
        return nUniq;
    }
}