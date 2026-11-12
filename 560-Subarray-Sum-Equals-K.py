class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dicti = {0:1}
        res = 0
        total = 0
        for i in range(len(nums)):
            total+=nums[i]
            freq = total-k
            x = dicti.get(freq,0)
            res+=x
            dicti[total]=dicti.get(total,0)+1
        return res

