class Solution {
    public List<Integer> luckyNumbers (int[][] matrix) {
        ArrayList<Integer> lucky = new ArrayList<>();
        ArrayList<Integer> index = new ArrayList<>();
        for(int i=0; i<matrix.length; i++) {
            int min = matrix[i][0];
            int minj = 0;
            for(int j=0; j<matrix[i].length; j++){
                if(matrix[i][j] < min) {
                    min = matrix[i][j];
                    minj = j;
                }
            }
            index.add(minj);
        }
        Iterator<Integer> mincol = index.iterator();
        int row = 0;
        while(mincol.hasNext()) {
            int minatcol = mincol.next();
            int maxval = 0;
            int maxrow = 0;
            for(int i=0; i<matrix.length; i++) {
                if(maxval<matrix[i][minatcol]) {
                    maxval = matrix[i][minatcol];
                    maxrow = i;
                }
            }
            if(maxrow == row) {
                lucky.add(matrix[row][minatcol]);
            }
            row++;
        }
        return lucky;
    }
}