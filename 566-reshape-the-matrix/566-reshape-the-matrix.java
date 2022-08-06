class Solution {
    public int[][] matrixReshape(int[][] mat, int r, int c) {
        int m = mat.length;
        int n = mat[0].length;
        if(m*n == r*c) {
            int[][] reshape = new int[r][c];
            int rr = 0, rc = 0;
            for(int[] row: mat) {
                for(int item: row) {
                    rr += rc/c;
                    rc = rc%c;
                    reshape[rr][rc] = item;
                    rc++;
                }
            }
            return reshape;
        }
        else
            return mat;
    }
}