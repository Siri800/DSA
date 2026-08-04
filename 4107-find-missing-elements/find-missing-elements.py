class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        max_n=max(nums)
        min_n=min(nums)
        s=set(nums)
        ans=[]
        for num in range(min_n+1,max_n):
            if num not in s:
                ans.append(num)
        return ans