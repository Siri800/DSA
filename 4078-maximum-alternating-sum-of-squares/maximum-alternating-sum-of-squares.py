class Solution:
    def maxAlternatingSum(self,nums):
        nums.sort(key=lambda x:x*x)
        squares=[x*x for x in nums]
        n=len(squares)
        return sum(squares[n//2:])-sum(squares[:n//2])