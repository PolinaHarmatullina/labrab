class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        ans = []
        nums = sorted(nums)
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                aim = target-nums[i]-nums[j]
                l = j+1
                r = len(nums)-1
                while l<r:
                    if nums[l]+nums[r]>aim:
                        r = r-1
                    elif nums[l]+nums[r]<aim:
                        l = l+1
                    else:
                        if [nums[i],nums[j],nums[l],nums[r]] not in ans:
                            ans.append([nums[i],nums[j],nums[l],nums[r]])
                        l = l+1
                        while l<r and nums[l-1] == nums[l]:
                            l = l+1
        return ans