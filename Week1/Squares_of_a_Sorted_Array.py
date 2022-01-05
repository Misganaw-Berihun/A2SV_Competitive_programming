class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = list(map(lambda a: a * a, nums))
        nums.sort()
        return nums
