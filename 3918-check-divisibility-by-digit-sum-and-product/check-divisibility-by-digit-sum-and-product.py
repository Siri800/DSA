class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s=0
        p=1
        x=n
        while x:
            digit=x%10
            s+=digit
            p*=digit
            x//=10
        return n%(s+p)==0