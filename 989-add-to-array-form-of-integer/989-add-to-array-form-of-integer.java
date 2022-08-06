class Solution {
    public List<Integer> addToArrayForm(int[] num, int k) {
        ArrayList<Integer> numAL = new ArrayList<>();
        ArrayList<Integer> kAL = new ArrayList<>();
        ArrayList<Integer> sum = new ArrayList<>();
        for(int i = 0; i<num.length; i++) {
            numAL.add(num[i]);
        }
        int len = numAL.size();
        while(k>0 || len > 0) {
            kAL.add(0, k%10);
            k/=10;
            len--;
        }
        for(int i = 1; i<=kAL.size() - num.length; i++) {
            numAL.add(0, 0);
        }
        int carry = 0;
        for(int i = numAL.size() - 1; i>=0; i--) {
            int total = carry + numAL.get(i) + kAL.get(i);
            carry = total / 10;
            sum.add(0,total%10);
        }
        if(carry>0)
            sum.add(0, carry);
        return sum;
    }
}