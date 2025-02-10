class Solution {
    public String clearDigits(String s) {
        StringBuffer str = new StringBuffer("");
        int ctr = 0;
        for(int i = 0; i<s.length(); i++) {
            char c = s.charAt(i);
            if('0'<= c && c<='9')
                str.deleteCharAt(str.length()-1);
            else
                str.append(""+c);
        }
        return str.toString();
    }
}