class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums_int = list(map(int,nums))
        nums_int.sort()

        return str(nums_int[len(nums) - k])
        
