class Solution:
    def sumZero(self, n: int) -> list[int]:
        arr = []
        st = n//2
        if n%2!=0:
            for i in range(-st,st+1):
                arr.append(i)
        else:
            for i in range(-st,st+1):
                if i==0:
                    continue
                else:
                    arr.append(i)
        return arr