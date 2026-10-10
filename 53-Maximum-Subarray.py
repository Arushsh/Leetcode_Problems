class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        res = 0
        maxi = -float('inf')
        for i in range(0,len(nums)):
            res = res+nums[i]
            if res >maxi:
                maxi=res
            if res<0:
                res=0
        return maxi
