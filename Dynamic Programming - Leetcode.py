# number 70, Easy
#number of ways to climb stairs
#uses fibonacci sequence, starting from 1, 2 for slightly more efficient solution
class Solution(object):
    def climbStairs(self, n):
        result = []
        a, b = 1, 2
        i = 0
        while i < n:
            result.append(a)
            a, b = b, a+b
            i += 1
        return result[n-1]