class Solution {
    public int maximumWealth(int[][] accounts) {
        int max = 0;
        for(int[] person:accounts) {
            int sum = 0;
            for(int acc: person) {
                sum += acc;
            }
            if(max<sum) {
                max = sum;
            }
        }
        return max;
    }
}