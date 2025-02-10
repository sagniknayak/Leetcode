class Solution {
    public String clearDigits(String s) {
        String str = "";
        int ctr = 0;
        for(int i = 0; i<s.length(); i++) {
            char c = s.charAt(i);
            if(Character.isDigit(c))
                str = str.substring(0,str.length()-1);
            else
                str += c;
            System.out.println(ctr);
            System.out.println(str);
        }
        return str;
    }
}