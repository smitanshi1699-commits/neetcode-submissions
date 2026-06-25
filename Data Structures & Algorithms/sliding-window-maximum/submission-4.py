class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        a=[]
        for left in range(len(nums)-k+1):
            right = left + k
            b = max(nums[left:right])
            a.append(b)
        return a
            
