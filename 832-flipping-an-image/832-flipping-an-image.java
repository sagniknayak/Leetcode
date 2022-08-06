class Solution {
    public int[][] flipAndInvertImage(int[][] image) {
        int n = image.length;
        int[][] flippedInverted = new int[n][n];
        for(int i = 0; i<n; i++){
            for(int j = 0; j<n; j++){
                flippedInverted[i][j] = 1^(image[i][n-1-j]);
            }
        }
        return flippedInverted;
    }
}