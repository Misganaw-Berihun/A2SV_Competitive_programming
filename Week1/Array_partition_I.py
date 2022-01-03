class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)
        sum = 0
        for i in range(0,len(nums),2):
            sum += nums_sorted[i]
        return sum
            
