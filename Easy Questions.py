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



#hardcoded version, but much easier to understand
'''class Solution(object):
    def romanToInt(self, s):
        total = 0
        for i in s:
            if i == 'I':
                total += 1
            elif i == 'V':
                total += 5
            elif i == 'X':
                total += 10
            elif i == 'L':
                total += 50
            elif i == 'C':
                total += 100
            elif i == 'D':
                total += 500
            elif i == 'M':
                total += 1000

        if 'IV' in s:
            total -= 2
        if 'IX' in s:
            total -= 2
        if 'XL' in s:
            total -= 20
        if 'XC' in s:
            total -= 20
        if 'CD' in s:
            total -= 200
        if 'CM' in s:
            total -= 200
        return total'''
# imagine not hardcoding it, but using a dictionary instead
class Solution(object):
    def romanToInt(self, s):
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        total = 0
        for i in range(len(s)):
            if i > 0 and roman[s[i]] > roman[s[i-1]]:
                total += roman[s[i]] - 2 * roman[s[i-1]]
            else:
                total += roman[s[i]]
        return total

print(Solution().romanToInt('MCMXCIV'))



# Description: Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive). Range sum of BST
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        if root == None: # if root is None, then we can return 0
            return 0
        if root.val < low: # if root.val < low, then all the left nodes are smaller than low, so we can skip them
            return self.rangeSumBST(root.right, low, high) 
        if root.val > high: # if root.val > high, then all the right nodes are bigger than high, so we can skip them
            return self.rangeSumBST(root.left, low, high)
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high) # if root.val is in the range, then we can add it to the sum and continue to search the left and right nodes


root = [10,5,15,3,7,null,18]
print(Solution().rangeSumBST(root, 7, 15))



# Merge Sorted Array
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        for i in range(n):
            nums1[m+i] = nums2[i]
        nums1.sort()
        return nums1

# Plus One
class Solution(object):
    def plusOne(self, digits):
        for i in range(len(digits)-1,-1,-1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits