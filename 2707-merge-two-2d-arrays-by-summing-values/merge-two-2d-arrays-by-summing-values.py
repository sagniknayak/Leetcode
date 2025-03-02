class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ptr1 = ptr2 = 0
        res = list()
        while ptr1<len(nums1) and ptr2<len(nums2):
            if nums1[ptr1][0] == nums2[ptr2][0]:
                res.append([nums1[ptr1][0],  nums1[ptr1][1] + nums2[ptr2][1]])
                ptr1+=1
                ptr2+=1
            elif nums1[ptr1][0] < nums2[ptr2][0]:
                res.append([nums1[ptr1][0],  nums1[ptr1][1]])
                ptr1+=1
            else:
                res.append([nums2[ptr2][0],  nums2[ptr2][1]])
                ptr2+=1
        else:
            if ptr1 == len(nums1):
                while ptr2 < len(nums2):
                    res.append([nums2[ptr2][0], nums2[ptr2][1]])
                    ptr2+=1
            else:
                while ptr1 < len(nums1):
                    res.append([nums1[ptr1][0], nums1[ptr1][1]])
                    ptr1+=1
        print(res)
        return res