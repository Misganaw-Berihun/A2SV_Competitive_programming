class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 1

        if(len(nums) == 0):
            return 0
        temp = nums[0]

        for i in range(len(nums)):
            if nums[i] != temp:
                nums[idx] = nums[i]
                idx += 1
                temp = nums[i]

        return idx
                
