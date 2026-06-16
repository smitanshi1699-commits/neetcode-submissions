from collections import OrderedDict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {value :index for index,value in enumerate(nums)}
        #print(a)
        for i in range(0,len(nums)):
            b= target -nums[i]
            if b in a:
                if a[b] != i:
                    return [i,a[b]]


        