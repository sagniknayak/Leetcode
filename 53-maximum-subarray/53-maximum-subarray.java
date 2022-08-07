class Solution {
    public int maxSubArray(int[] nums) {
        int max = Integer.MIN_VALUE;
        int ctr = 0;
        for(int num: nums) {
            if(num>0)
                ctr++;
            if(num>max)
                max = num;
        }
        if(ctr == 0 || ctr == 1)
            return max;
        else {
            int max_till_now = (nums[0]<0)?0:nums[0];
            int max_sum = nums[0];
            for(int i=1; i<nums.length; i++) {
                max_sum = Math.max(max_sum, max_till_now + nums[i]);
                max_till_now += nums[i];
                max_till_now = (max_till_now < 0)?0:max_till_now;
            }
            return max_sum;
        }
    }
}