class Solution {
    public String largestOddNumber(String num) {
        int loc = -1;
        for(int i = num.length()-1; i >= 0; i--){
            String check = ""+num.charAt(i);
            if(Integer.parseInt(check)%2==1){
                loc = i;
                break;
            }
        }
        return num.substring(0,loc+1);
    }
}