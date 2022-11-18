#takes a set of numbers and a target number. Returns the indices of two numbers from the set that add up to the target number
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]               
print(Solution().twoSum([2, 7, 11, 15], 9)) 



class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        if x == x[::-1]:
            return True        
print(Solution().isPalindrome(121))



class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1
print(Solution().removeDuplicates([1, 1, 2]))
