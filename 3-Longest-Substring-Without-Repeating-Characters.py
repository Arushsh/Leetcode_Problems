class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        low = 0
        idx = {}
        res = -float('inf')
        if len(s)==0:
            return 0
        for high,ch in enumerate(s):
            if ch in idx and idx[ch]>=low:
                low = idx[ch]+1
            idx[ch]=high
            res=max(res,high-low+1)
        return res