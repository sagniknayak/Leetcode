class Solution {
    public int[] runningSum(int[] nums) {
        int n = nums.length;
        int[] r_sum = new int[n];
        r_sum[0] = nums[0];
        for(int i = 1; i < n; i++) {
            r_sum[i] = r_sum[i-1] + nums[i];
        }
        return r_sum;
        
    }
}