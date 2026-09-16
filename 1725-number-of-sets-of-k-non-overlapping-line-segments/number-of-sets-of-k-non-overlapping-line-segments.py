class Solution:
    def numberOfSets(self,n,k):
        from math import comb
        return comb(n+k-1,2*k)%(10**9+7)