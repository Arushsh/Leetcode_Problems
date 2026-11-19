class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        res = []
        fin = []
        for i in image:
            res.append(i[::-1])
        for j in range(len(res)):
            for x in range(len(res[j])):
                if res[j][x]==0:
                    res[j][x]=1
                else:
                    res[j][x]=0
        return res
                    