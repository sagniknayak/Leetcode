class Solution {
    public String largestOddNumber(String num) {
        int loc = -1;
        for(int i = num.length()-1; i >= 0; i--){
            if(Integer.parseInt(""+num.charAt(i))%2==1){
                loc = i;
                break;
            }
        }
        return num.substring(0,loc+1);
    }
}