class Solution:
    def maximumSum(self, arr: list[int]) -> int:
        nodelete=arr[0]
        onedelete=-float('inf')
        res=arr[0]
        for i in range(1,len(arr)):
            prevno=nodelete
            prevone=onedelete
            v1=nodelete+arr[i]
            v2=arr[i]
            nodelete=max(v1,v2)
            if prevone==-float('inf'):
                v3=arr[i]
            else:
                v3=prevone+arr[i]
            onedelete=max(prevno,v3)
            res=max(res,max(onedelete,nodelete))
        return res