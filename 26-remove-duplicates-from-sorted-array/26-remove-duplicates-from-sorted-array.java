class Solution {
    public int removeDuplicates(int[] nums) {
        int prev = Integer.MIN_VALUE;
        int ptr = 0;
        for(int val: nums) {
            if(val == prev)
                continue;
            nums[ptr++] = val;
            prev = val;
        }
        return ptr;
    }
}