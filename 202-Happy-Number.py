class Solution:
    def isHappy(self, n: int) -> bool:
        def sqre(n):
            sums = 0
            while (n>0):
                d = n%10
                n=n//10
                sums = sums+d*d
            return sums
        slow = n
        fast = n
        while(fast!=1):
            slow = sqre(slow)
            fast = sqre(fast)
            fast = sqre(fast)
            if slow==fast and slow!=1:                
                return False
        return True