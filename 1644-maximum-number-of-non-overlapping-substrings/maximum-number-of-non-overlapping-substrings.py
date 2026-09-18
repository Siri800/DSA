class Solution:
    def maxNumOfSubstrings(self,s):
        first=[len(s)]*26
        last=[-1]*26
        for i,c in enumerate(s):
            x=ord(c)-97
            first[x]=min(first[x],i)
            last[x]=i
        ans=[]
        end=-1
        for i in range(len(s)):
            x=ord(s[i])-97
            if i!=first[x]:
                continue
            r=last[x]
            j=i
            ok=True
            while j<=r:
                y=ord(s[j])-97
                if first[y]<i:
                    ok=False
                    break
                r=max(r,last[y])
                j+=1
            if ok:
                if i>end:
                    ans.append(s[i:r+1])
                    end=r
                else:
                    ans[-1]=s[i:r+1]
                    end=r
        return ans