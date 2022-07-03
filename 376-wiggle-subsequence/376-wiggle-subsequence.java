class Solution {
    public int wiggleMaxLength(int[] nums) {
        int pos_sign_change = 1, neg_sign_change = 1;
        for(int i=1; i<nums.length; i++) {
                if(nums[i-1]<nums[i])
                    pos_sign_change = neg_sign_change + 1;
                else if(nums[i-1]>nums[i])
                    neg_sign_change = pos_sign_change + 1;
        }
        return Math.max(pos_sign_change, neg_sign_change);
    }
}