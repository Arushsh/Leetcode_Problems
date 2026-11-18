class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        ins = False
        res = []

        for i in range(len(intervals)):
            start = intervals[i][0]

            if ins == False and start >= newInterval[0]:
                res.append(newInterval)
                ins = True

            res.append(intervals[i])

        # Missing condition
        if not ins:
            res.append(newInterval)

        fin = []

        start1 = res[0][0]
        end1 = res[0][1]

        for i in range(1, len(res)):
            start2 = res[i][0]
            end2 = res[i][1]

            if end1 >= start2:
                end1 = max(end1, end2)
                continue

            fin.append([start1, end1])

            start1 = start2
            end1 = end2

        fin.append([start1, end1])

        return fin