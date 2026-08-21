class Solution:
    def findKthSmallest(self,coins,k):
        from math import gcd
        useful=[]
        for coin in sorted(coins):
            if not any(coin%x==0 for x in useful):
                useful.append(coin)
        coins=useful
        n=len(coins)
        def count(amount):
            total=0
            for mask in range(1,1<<n):
                lcm=1
                bits=0
                for i in range(n):
                    if mask>>i&1:
                        bits+=1
                        lcm=lcm//gcd(lcm,coins[i])*coins[i]
                        if lcm>amount:
                            break
                else:
                    if bits%2:
                        total+=amount//lcm
                    else:
                        total-=amount//lcm
            return total
        left=1
        right=min(coins)*k
        while left<right:
            middle=(left+right)//2
            if count(middle)>=k:
                right=middle
            else:
                left=middle+1
        return left