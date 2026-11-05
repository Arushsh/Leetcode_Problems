class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        res = 0
        for i in arr1:
            cnt=0
            for j in arr2:
                if (abs(i-j))<=d:
                    break
                else:
                    cnt+=1
            if cnt==len(arr2):
                res+=1
        return res