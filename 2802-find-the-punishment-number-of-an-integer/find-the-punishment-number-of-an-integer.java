class Solution {
    public int punishmentNumber(int n) {
        int sum = 0;
        for(int i = 1; i<=n; i++) {
            int sq = i*i;
            sum+=(sum_partition(i, sq))?sq:0;
        }
        return sum;
    }
    boolean sum_partition(int num, int lftprt) {
        int rtprt = 0;
        for(int l=0; lftprt>0; l++) {
            rtprt += (lftprt%10)*Math.pow(10,l);
            lftprt /= 10;
            if(num == lftprt+rtprt || sum_partition(num-rtprt, lftprt))
                return true;
        }
        return false;
    }
}