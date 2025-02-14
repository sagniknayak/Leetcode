class Solution {
    public int reverse(int x) {
        int dup = x;
        x = Math.abs(x);
        int reverse = 0, dig =0;
        long val = 0;
        while(x>0){
            dig = x%10;
            val = ((long)reverse)*10 + dig;
            if(val > Integer.MAX_VALUE){
               return 0;
            }
            reverse = (int)val;   
            x/=10;
        }
        return reverse*((dup<0)?-1:1);
    }
}