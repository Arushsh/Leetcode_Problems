class Solution:
    def arraySign(self, nums: list[int]) -> int:
        prod = 1
        for i in nums:
            prod = prod * i
        if prod < 0:
            return -1
        elif prod == 0:
            return 0
        else:
            return 1