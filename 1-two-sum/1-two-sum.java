class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] pair = new int[2];
        for(int i=0; i<nums.length - 1; i++) {
            int a = nums[i];
            for(int j=i+1; j<nums.length; j++) {
                if(target-a == nums[j]) {
                    pair[0] = i;
                    pair[1] = j;
                    break;
                }
            }
        }
        return pair;
    }
}