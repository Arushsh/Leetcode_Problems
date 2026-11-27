class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        a = set(nums)-{0}
        return len(a)
