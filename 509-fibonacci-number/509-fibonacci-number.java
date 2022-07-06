class Solution {
    public int fib(int n) {
        int a = 0, b = 1;
        int s = 0;
        if(n==0)
            s=a;
        else if(n==1)
            s=b;
        else {
            for(int i = 2; i <= n; i++) {
                s = a+b;
                a = b;
                b = s;
            }
        }
        return s;        
    }
}