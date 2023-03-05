'''
def twoSums(list, target):
    sums = {}
    for i in range(len(list)):
        if target - list[i] in sums:
            return [sums[target-list[i]],i]
        else:
            sums[list[i]] = i
            
list = [2,8,12,15]
print(twoSums(list, 20))
'''

class Solution:
    def twoSum(self, nums, target):
        
        d = {}
        for i, v in enumerate(nums):
            r = target - v
            if r in d: 
                return [d[r], i]
            d[v] = i


nums = [2,7,11,15]
obj = Solution()
print(obj.twoSum(nums, 4))
