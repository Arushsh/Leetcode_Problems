class Solution:
    def findLucky(self, arr: list[int]) -> int:
        my_list = [0] * 501
        for i in arr:
            my_list[i] = my_list[i]+1
        for j in range(500,0,-1):
            if j==my_list[j]:
                print(j)
                return j
        return -1