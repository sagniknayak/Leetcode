class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        ArrayList<Integer> arr = new ArrayList<>();
        int m = matrix.length;
        int n = matrix[0].length;
        System.out.println(m+" "+n);
        int srow = 0, erow = m-1, scol = 0, ecol = n-1;
        while(srow<=erow && scol<=ecol){
            System.out.println(srow + " "+ erow);
            for(int j=scol; j<=ecol; j++)
                arr.add(matrix[srow][j]);
            for(int i=srow+1; i<=erow; i++)
                arr.add(matrix[i][ecol]);
            for(int j=ecol-1; j>=scol; j--){
                if(srow==erow)
                    break;
                arr.add(matrix[erow][j]);
            }
            for(int i=erow-1; i>srow; i--){
                if(scol==ecol)
                    break;
                arr.add(matrix[i][scol]);
            }
            srow++;
            erow--;
            scol++;
            ecol--;
        }
        return arr;
    }
}