class Solution:
    def minSumSquareDiff(self,nums1,nums2,k1,k2):
        diff=[abs(a-b) for a,b in zip(nums1,nums2)]
        k=k1+k2
        if sum(diff)<=k:
            return 0
        left,right=0,max(diff)
        while left<right:
            mid=(left+right)//2
            need=sum(max(0,x-mid) for x in diff)
            if need<=k:
                right=mid
            else:
                left=mid+1
        level=left
        remaining=k-sum(max(0,x-level) for x in diff)
        ans=0
        for x in diff:
            value=min(x,level)
            if value>0 and remaining>0 and x>=level:
                value-=1
                remaining-=1
            ans+=value*value
        return ans