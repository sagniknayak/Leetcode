class Solution {
    public int oddCells(int m, int n, int[][] indices) {
        int[][] matrix = new int[m][n];
        for(int[] op: indices) {
            for(int i = 0; i < n; i++) {
                matrix[op[0]][i] += 1;
            }
            for(int i = 0; i < m; i++) {
                matrix[i][op[1]] += 1;
            }
        }
        int ctr = 0;
        for(int[] row: matrix) {
            for(int item: row) {
                if(item%2 == 1)
                    ctr++;
            }
        }
        return ctr;
    }
}