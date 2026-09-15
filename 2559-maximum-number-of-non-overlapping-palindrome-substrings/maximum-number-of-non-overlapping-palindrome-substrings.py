class Solution:
    def maxPalindromes(self,s,k):
        n=len(s)
        dp=[0]*(n+1)
        for i in range(1,n+1):
            dp[i]=dp[i-1]
            if i>=k:
                x=s[i-k:i]
                if x==x[::-1]:
                    dp[i]=max(dp[i],dp[i-k]+1)
            if i>=k+1:
                x=s[i-k-1:i]
                if x==x[::-1]:
                    dp[i]=max(dp[i],dp[i-k-1]+1)
        return dp[n]