class Solution:
    def minSumOfLengths(self,arr,target):
        n=len(arr)
        best=[float('inf')]*(n+1)
        ans=float('inf')
        left=0
        curr=0
        for right in range(n):
            curr+=arr[right]
            while curr>target:
                curr-=arr[left]
                left+=1
            if curr==target:
                length=right-left+1
                if best[left]!=float('inf'):
                    ans=min(ans,length+best[left])
                best[right+1]=min(best[right],length)
            else:
                best[right+1]=best[right]
        return -1 if ans==float('inf') else ans