class Solution {
    public boolean isPowerOfFour(int n) {
        double pow = Math.log(n)/Math.log(4);
        int power = (int)pow;
        if(power == pow)
            return true;
        else
            return false;
    }
}