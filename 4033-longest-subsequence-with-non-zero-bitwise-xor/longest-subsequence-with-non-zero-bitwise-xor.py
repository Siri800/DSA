class Solution:
    def longestSubsequence(self,nums):
        total_xor=0
        for number in nums:
            total_xor^=number
        if total_xor!=0:
            return len(nums)
        for number in nums:
            if number!=0:
                return len(nums)-1
        return 0