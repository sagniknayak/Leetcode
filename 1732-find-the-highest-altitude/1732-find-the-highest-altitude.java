class Solution {
    public int largestAltitude(int[] gain) {
        int alti = 0, maxAlti = 0;
        for(int gn: gain) {
            alti += gn;
            if(alti>maxAlti)
                maxAlti = alti;
        }
        return maxAlti;
    }
}