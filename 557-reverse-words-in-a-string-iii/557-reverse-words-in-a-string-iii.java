class Solution {
    public String reverseWords(String s) {
        String newword = "", word = "";
        s = s.trim() + " ";
        int len = s.length();
        for(int i = 0; i<len; i++) {
            char k = s.charAt(i);
            if(k == ' '){
                newword += word + " ";
                word = "";
            }
            else {
                word = k + word;
            }
        }
        return newword.trim();
            
    }
}