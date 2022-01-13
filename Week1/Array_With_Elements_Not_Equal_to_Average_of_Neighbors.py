class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        median = 0 #keeps the middle element
        l= len(nums)
        result = [0]*len(nums) # creates a zero list
        even_idx = 0 #even indices of result
        odd_idx = 1 #odd indices of result

        if l % 2:#does nums has odd number of elements?
            median = nums[l // 2]
        else:
            median = (nums[l // 2 - 1] + nums[l // 2]) / 2

        for idx in range(len(nums)):
            if nums[idx] < median:
                result[odd_idx] = nums[idx]
                odd_idx += 2
            else:
                result[even_idx] = nums[idx]
                even_idx += 2

        return result
