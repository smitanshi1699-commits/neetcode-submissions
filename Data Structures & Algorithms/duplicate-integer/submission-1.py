class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        b = len(nums)
        a = False
        for i in range(0,b-1):
            if nums[i] == nums[i+1]:
                a = True
        return a