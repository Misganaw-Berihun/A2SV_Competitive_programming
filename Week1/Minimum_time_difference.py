class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        convert = lambda a: int(a[0:2])*60 + int(a[3:])
        minutes = list(map(convert,timePoints))
        min_diff = float(inf)
        n = len(minutes)

        minutes.sort()

        min_compare = list( zip(
                          minutes ,
                          minutes[1:n] + [minutes[0]]
                        ))

        for k1 ,k2 in min_compare:
            dif = min(abs(k2 - k1), abs(1440 - k1 + k2))

            if dif < min_diff:
                min_diff = dif

        return min_diff

        
