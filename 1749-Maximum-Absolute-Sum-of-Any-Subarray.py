class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        def mini(arr):
            best=arr[0]
            res=arr[0]
            for i in range(1,len(arr)):
                best=min(best+arr[i],arr[i])
                res=min(res,best)
            return res
        def maxi(arr):
            best=arr[0]
            res=arr[0]
            for i in range(1,len(arr)):
                best=max(best+arr[i],arr[i])
                res=max(res,best)
            return res
        #x=abs(mini(nums))
        #y=abs(maxi(nums))
        #return max(x,y)
        return max(abs(mini(nums)),abs(maxi(nums)))