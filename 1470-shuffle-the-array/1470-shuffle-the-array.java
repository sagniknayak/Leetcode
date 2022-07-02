class Solution {
    public int[] shuffle(int[] nums, int n) {
        int[] shuffled = new int[2*n];
        int ctr = 0;
        for(int i=0; i<2*n; i+=2) {
            shuffled[i] = nums[ctr];
            shuffled[i+1] = nums[ctr+n];
            ctr++;
        }
        return shuffled;
    }
}