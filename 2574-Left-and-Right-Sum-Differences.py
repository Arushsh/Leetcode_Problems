class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        r = sum(nums)
        l = 0
        res = []
        for i in nums:
            r-=i
            res.append(abs(l-r))
            l+=i
        return res
            
