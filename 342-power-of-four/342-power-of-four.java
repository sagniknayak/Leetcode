class Solution {
    public boolean isPowerOfFour(int n) {
        double pow = Math.log(n)/Math.log(4);
        return (pow == (int)pow)?true:false;
    }
}