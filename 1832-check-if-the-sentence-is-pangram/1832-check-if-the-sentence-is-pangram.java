class Solution {
    public boolean checkIfPangram(String sentence) {
        sentence = sentence.toUpperCase();
        boolean flag = true;
        for(int i = 65; i <= 90; i++) {
            if(sentence.indexOf((char)i) == -1) {
                flag = false; break;
            }
        }
        return flag;
    }
}