class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_dict = {}
        for num in nums:
            if num not in num_dict:
                num_dict[num] = 1
                
        for num in range(len(nums)+1):
            if num not in num_dict:
                return num