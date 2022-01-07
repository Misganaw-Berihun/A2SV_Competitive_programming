class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        dist_speed = list(zip(dist,speed))
        dist_speed.sort(key = lambda a: (a[0]/a[1]))
        time_to_arrive = list(map(lambda a: (a[0]/a[1]),dist_speed))
        count = 0

        for i in range(len(time_to_arrive)):
            if time_to_arrive[i] > i:
                count += 1
            else:
                break

        return count







        
