class Solution:
    def sumGame(self, num: str) -> bool:
        n=len(num)
        left=num[:n//2]
        right=num[n//2:]
        s1=sum(int(x) for x in left if x!='?')
        s2=sum(int(x) for x in right if x!='?')
        q1=left.count('?')
        q2=right.count('?')
        if (q1+q2)%2==1:
            return True
        return s1-s2!=9*(q2-q1)//2