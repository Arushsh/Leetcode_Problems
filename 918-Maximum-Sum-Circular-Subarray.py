
class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        best = nums[0]
        ans = nums[0]
        minans = nums[0]

        # First Kadane: Maximum subarray sum
        for i in range(1, len(nums)):
            x = best + nums[i]
            y = nums[i]

            best = max(x, y)
            ans = max(ans, best)

        # Handle all-negative arrays
        if ans < 0:
            return ans

        # Reset best before minimum Kadane
        best = nums[0]
        minans = nums[0]

        # Second Kadane: Minimum subarray sum
        for j in range(1, len(nums)):
            c = best + nums[j]
            d = nums[j]

            best = min(c, d)
            minans = min(minans, best)

        ans1 = ans
        ans2 = sum(nums) - minans

        return max(ans1, ans2)
