class Solution {
    public int[] plusOne(int[] digits) {
        ArrayList<Integer> number= new ArrayList<Integer>();
        int carry = 1;
        int index = digits.length - 1;
        for(int i = index; i>=0; i--) {
            int total = digits[i]+carry;
            carry = total/10;
            total = total%10;
            number.add(0,total);
        }
        if(carry == 1){
            number.add(0, 1);
        }
        int n = number.size();
        int[] num = new int[n];
        for(int i=0;i<n;i++)
            num[i] = number.get(i);
        return num;
    }
}