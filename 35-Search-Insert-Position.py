class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        a = 0
        b = len(nums)
        while(a<b):
            mid = (a+b)//2
            if nums[mid]>=target:
                b=mid
            else:
                a=mid+1
        return a
            
            