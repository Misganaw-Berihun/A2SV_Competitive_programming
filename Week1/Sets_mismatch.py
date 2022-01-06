class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        occurence = Counter(nums)
        result = []

        for key,value in occurence.items():
            if value == 2:
                result.append(key)

        for i in range(1,len(nums) + 1):
            if i not in occurence:
                result.append(i)

        return result

        
