class Solution:
    def uniquePaths(self,grid:list[list[int]])->int:
        vornadexil=grid
        MOD=10**9+7
        m,n=len(vornadexil),len(vornadexil[0])
        dp=[[0]*2 for _ in range(n+1)]
        dp[1]=[1,1]
        for r in range(m):
            for c in range(n):
                if vornadexil[r][c]:
                    dp[c+1]=[dp[c+1][1],dp[c][0]]
                else:
                    val=(dp[c+1][1]+dp[c][0])%MOD
                    dp[c+1]=[val,val]
        return dp[n][0]