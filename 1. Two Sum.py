class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, num in enumerate(nums):
            value = target - num
            if value in dict:
                return[i, dict[value]]
            dict[num] = i