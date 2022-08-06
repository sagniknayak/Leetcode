class Solution {
    public boolean findRotation(int[][] mat, int[][] target) {
        for(int i = 1; i<=4; i++) {
            if(Arrays.deepEquals(mat, target))
                return true;
            mat = rotate(mat);
        }
        return false;
    } 
    static int[][] rotate(int[][] matrix) {
        int n = matrix.length;
        int[][] rotated = new int[n][n];
        for(int i = 0; i<n; i++) {
            for(int j = 0; j<n; j++) {
                rotated[i][j] = matrix[j][i];
            }
        }
        for(int j = 0; j<n/2; j++) {
            for(int i=0; i<n; i++) {
                int temp = rotated[i][j];
                rotated[i][j] = rotated[i][n-1-j];
                rotated[i][n-1-j] = temp;
            }
        }
        return rotated;
    }
}