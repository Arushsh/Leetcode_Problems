class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res = []
        for i in nums1:
            idx = nums2.index(i)+1
            found =  False
            
                
            for j in range(idx,len(nums2)):
                if nums2[j]>i:
                    res.append(nums2[j])
                    found = True
                    break
            
            if not found:
                res.append(-1)
        return res