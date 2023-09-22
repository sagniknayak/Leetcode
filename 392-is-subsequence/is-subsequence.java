class Solution {
    public boolean isSubsequence(String s, String t) {
        int slen = s.length(), tlen = t.length();
        int p1 = 0, p2 = 0;
        while(p1 < slen && p2 < tlen) {
            if(s.charAt(p1) == t.charAt(p2)) {
                p1++;
            }
            p2++;
        }
        if(p1 == slen) {
            return true;
        }
        else {
            return false;
        }
    }
}