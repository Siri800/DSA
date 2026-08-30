class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n=len(nums)
        min_idx=0
        max_idx=0
        for i in range(n):
            if nums[i]<nums[min_idx]:
                min_idx=i
            if nums[i]>nums[max_idx]:
                max_idx=i
        a=min(min_idx,max_idx)
        b=max(min_idx,max_idx)
        left=b+1
        right=n-a
        both=a+1+(n-b)
        return min(left,right,both)