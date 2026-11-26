class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        x = []
        n = len(names)
        for i in range(n):
            x.append((heights[i], names[i]))
        print(x)
        x.sort(reverse=True)
        z = []
        for i in range(n):
            z.append(x[i][1])
        return z