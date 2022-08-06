class Solution {
    public int[] sumZero(int n) {
        int[] nUniq = new int[n];
        int half = n/2;
        for(int i=0; i<n/2; i++) {
            nUniq[i] = -half;
            nUniq[n-1-i] = half;
            half--;
        }
        return nUniq;
    }
}