class Solution {
    public int candy(int[] ratings) {
        int n = ratings.length;
        int[] from_left = new int[n];
        int[] from_right = new int[n];
        for(int i=0; i<n; i++)
            from_left[i] = from_right[i] = 1;
        
        for(int i=1; i<n; i++) {
            if(ratings[i]>ratings[i-1])
                from_left[i] = from_left[i-1]+1;
        }
        
        for(int i=n-2; i>=0; i--) {
            if(ratings[i]>ratings[i+1])
                from_right[i] = from_right[i+1]+1;
        }
        
        int total = 0;
        for(int i=0;i<n;i++) {
            total += Math.max(from_left[i], from_right[i]);
        }
        return total;
    }
}