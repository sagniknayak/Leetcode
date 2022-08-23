class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] result = {-1,-1};
        if(nums.length == 0)
            return result;
        result[0] = this.lowerlimit(nums, target);
        result[1] = this.upperlimit(nums, target);
        return result;
    }
    public int lowerlimit(int[] nums, int target) {
        int start = 0, end = nums.length - 1, res = -1, mid = 0;
        while(start<=end) {
            mid = (start+end)/2;
            if(nums[mid]>=target){
                if(nums[mid] == target)
                    res = mid;
                end = mid-1;
            }
            else
                start = mid+1;
        }
        return res;
    }
    
    public int upperlimit(int[] nums, int target) {
        int start = 0, end = nums.length - 1, res = -1, mid = 0;
        while(start<=end) {
            mid = (start+end)/2;
            if(nums[mid]<=target){
                if(nums[mid] == target)
                    res = mid;
                start = mid+1;
            }
            else
                end = mid-1;
        }
        return res;
    }
    
}