class Solution:
    def minInsertions(self, s: str) -> int:
        add = 0
        need= 0
        for i in s:
            if i == '(':
                if need%2==1:
                    add+=1
                    need-=1
                need+=2
            else:
                need-=1
                if need<0:
                    add+=1
                    need+=2
        return add+need