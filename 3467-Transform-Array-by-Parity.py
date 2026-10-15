class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        countEven=0
        countOdd=0
        for i in range(len(nums)):
            if nums[i]%2==0:
                countEven+=1
            else:
                countOdd+=1
        return [0] * countEven + [1] * countOdd