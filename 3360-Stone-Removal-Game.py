class Solution:
    def canAliceWin(self, n: int) -> bool:
        alice = 1
        c = 10
        if(n<c):
            return False
        while(n>=0):
            n=n-c
            c = c-1
            alice+=1
        if alice % 2==0:
            return False
        return True