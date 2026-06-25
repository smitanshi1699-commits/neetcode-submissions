class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        max_window = 0
        a=[]
        for left in range(len(nums)-k+1):
            right = left + k
            b = max(nums[left:right])
            a.append(b)
            left +=1
        return a
            
