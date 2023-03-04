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
        for i, j in enumerate(nums):
            r = target - j
            if r in d: 
                return [d[r], i]
            d[j] = i


nums = [2,7,11,15]
obj = Solution()
print(obj.twoSum(nums, 17))

'''
class Solution(object):
   def twoSum(self, nums, target):
      required = {}
      for i in range(len(nums)):
         if target - nums[i] in required:
            return [required[target - nums[i]],i]
         else:
            required[nums[i]]=i
input_list = [2,8,12,15]
ob1 = Solution()
print(ob1.twoSum(input_list, 20))
'''