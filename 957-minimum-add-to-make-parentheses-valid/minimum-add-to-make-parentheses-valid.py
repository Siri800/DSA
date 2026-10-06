class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        bal=0
        ans=0
        for ch in s:
            if ch=='(':
                bal+=1
            else:
                if bal>0:
                    bal-=1
                else:
                    ans+=1
        return ans+bal
