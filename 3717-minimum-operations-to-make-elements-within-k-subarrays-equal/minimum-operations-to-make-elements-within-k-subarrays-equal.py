from typing import List
class Solution:
    def minOperations(self,nums:List[int],x:int,k:int)->int:
        n=len(nums)
        values=sorted(set(nums))
        m=len(values)
        pos={v:i for i,v in enumerate(values)}
        count=[0]*(m+1)
        total=[0]*(m+1)
        def update(tree,i,delta):
            i+=1
            while i<=m:
                tree[i]+=delta
                i+=i&-i
        def query(tree,i):
            result=0
            while i>0:
                result+=tree[i]
                i-=i&-i
            return result
        def kth(tree,k):
            index=0
            bit=1<<(m.bit_length()-1)
            while bit:
                next_index=index+bit
                if next_index<=m and tree[next_index]<k:
                    index=next_index
                    k-=tree[next_index]
                bit>>=1
            return index
        costs=[]
        window_sum=0
        for i in range(x):
            update(count,pos[nums[i]],1)
            update(total,pos[nums[i]],nums[i])
            window_sum+=nums[i]
        for start in range(n-x+1):
            median_index=kth(count,(x+1)//2)
            median=values[median_index]
            left_count=query(count,median_index+1)
            left_sum=query(total,median_index+1)
            right_count=x-left_count
            right_sum=window_sum-left_sum
            cost=median*left_count-left_sum
            cost+=right_sum-median*right_count
            costs.append(cost)
            if start<n-x:
                old=nums[start]
                new=nums[start+x]
                update(count,pos[old],-1)
                update(total,pos[old],-old)
                update(count,pos[new],1)
                update(total,pos[new],new)
                window_sum+=new-old
        infinity=float('inf')
        previous=[0]*(n+1)
        for j in range(1,k+1):
            current=[infinity]*(n+1)
            for i in range(1,n+1):
                current[i]=current[i-1]
                if i>=x:
                    candidate=previous[i-x]+costs[i-x]
                    current[i]=min(current[i],candidate)
            previous=current
        return previous[n]