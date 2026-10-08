class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        arr = [0]* (n+1)
        print(arr)
        for i in nums:
            if i>=1 and i<=n:
                arr[i] = arr[i]+1
        for j in range(1,n+1):
            if arr[j]==0:
                return j
        return n +1