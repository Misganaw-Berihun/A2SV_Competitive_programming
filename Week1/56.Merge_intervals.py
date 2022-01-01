class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key = lambda a: a[0])#sort by first elment of the list
        start = intervals[0][0]
        end = intervals[0][1]

        merged = []
        for i in range(1,len(intervals)):
            if intervals[i][0] <= end:
                end = max(end, intervals[i][1])
            else:
                merged.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]

        merged.append([start, end])

        return merged
