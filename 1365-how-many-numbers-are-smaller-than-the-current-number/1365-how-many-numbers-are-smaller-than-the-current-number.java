class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int[] lesserThan = new int[nums.length];
        for(int i = 0; i<nums.length; i++) {
            int ctr = 0;
            for(int j = 0; j<nums.length; j++) {
                if(nums[i]>nums[j]){
                    ctr++;
                }
            }
            lesserThan[i] = ctr;
        }
        return lesserThan;
    }
}