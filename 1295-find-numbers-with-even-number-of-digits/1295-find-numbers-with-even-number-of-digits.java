class Solution {
    public int findNumbers(int[] nums) {
        int ctr = 0;
        for(int num: nums) {
            int dig = (int)Math.log10(num);
            if((dig+1)%2==0)
                ctr++;
        }
        return ctr;
    }
}