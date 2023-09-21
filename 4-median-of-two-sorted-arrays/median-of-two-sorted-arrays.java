import java.util.*;
class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        ArrayList<Integer> op = new ArrayList<>();
        int l1 = nums1.length, l2 = nums2.length;
        int median = l1+l2;
        double ans = 0.0;
        int p1 = 0, p2 = 0;
        while(p1<l1 && p2<l2) {
            if(nums1[p1]<nums2[p2]) {
                op.add(nums1[p1++]);
            }
            else {
                op.add(nums2[p2++]);
            }
        }
        int[] residue = (l1-1 - p1 < l2-1 - p2)?nums2:nums1;
        int p_res = (l1-1 - p1 < l2-1 - p2)?p2:p1;
        if(median%2==1) {
            median /= 2;
            ans = (median<op.size())?op.get(median):residue[p_res+(median - op.size())];
        }
        else {
            median /= 2;
            double v1 = (median-1<op.size())?op.get(median-1):residue[p_res+(median-1 - op.size())];
            double v2 = (median<op.size())?op.get(median):residue[p_res+(median - op.size())];
            ans = (v1+v2)/2.0;
        }
        return ans;
        
    }
}