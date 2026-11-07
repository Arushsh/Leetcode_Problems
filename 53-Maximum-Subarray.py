class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        best = nums[0]
        ans = nums[0]
        for i in range(1,len(nums)):
            a = best + nums[i]
            b = nums[i]
            best = max(a,b)
            ans = max(best,ans)
        return ans