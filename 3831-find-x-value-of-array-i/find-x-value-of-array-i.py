class Solution:
    def resultArray(self,nums,k):
        ans=[0]*k
        dp=[0]*k
        for num in nums:
            num%=k
            ndp=[0]*k
            ndp[num]+=1
            for r in range(k):
                ndp[r*num%k]+=dp[r]
            dp=ndp
            for r in range(k):
                ans[r]+=dp[r]
        return ans