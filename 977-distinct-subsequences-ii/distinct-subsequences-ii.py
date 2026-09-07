class Solution:
    def distinctSubseqII(self,s):
        MOD=10**9+7
        dp=[0]*26
        for character in s:
            index=ord(character)-ord('a')
            total=sum(dp)+1
            dp[index]=total%MOD
        return sum(dp)%MOD