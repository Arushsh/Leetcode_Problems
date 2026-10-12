class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # fin = nums1+nums2
        # fin.sort()
        # if len(fin)%2!=0:
        #     return fin[(len(fin)//2)]
        # else:
        #     return (fin[len(fin)//2]+fin[(len(fin)//2-1)])/2
        n = len(nums1)
        m = len(nums2)
        i = 0
        j = 0
        m1 = 0
        m2 = 0
        for c in range((n+m)//2+1):
            m2=m1
            if i<n and j<m:
                if nums1[i]<nums2[j]:
                    m1=nums1[i]
                    i+=1
                else:
                    m1=nums2[j]
                    j+=1
            elif(i<n):
                m1=nums1[i]
                i+=1
            else:
                m1=nums2[j]
                j+=1
        if (n+m)%2==1:
            return float(m1)
        else:
            return (float(m1)+float(m2))/2.0