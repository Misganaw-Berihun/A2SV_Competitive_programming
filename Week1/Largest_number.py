class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        num_str = list(map(str,nums))

        for i in range(len(num_str) - 1,0,-1):
            for j in range(len(num_str) - 1):
                if num_str[j] + num_str[j + 1] < num_str[j+1] + num_str[j]:
                    num_str[j],num_str[j+1] = num_str[j+1],num_str[j]

        return str(int(''.join(num_str)))



        
