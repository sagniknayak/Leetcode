class Solution {
    public int reverse(int x) {
        int dup = x;
        x = Math.abs(x);
        int reverse = 0, dig =0;
        long val = 0;
        while(x>0){
            dig = x%10;
            if(reverse > (Integer.MAX_VALUE-dig)/10){
               return 0;
            }
            reverse = reverse*10 + dig;   
            x/=10;
        }
        return reverse*((dup<0)?-1:1);
    }
}