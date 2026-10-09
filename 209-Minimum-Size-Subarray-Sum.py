class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        res = float('inf')
        low=0
        high=0
        tsum=0
        while(high<len(nums)):
            tsum = tsum+nums[high]
            while(tsum>=target):
                leng = high-low+1
                res = min(res,leng)
                tsum = tsum - nums[low]
                low+=1
            high+=1
        return 0 if res==float('inf') else res