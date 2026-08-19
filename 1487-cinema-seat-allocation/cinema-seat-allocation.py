class Solution:
    def maxNumberOfFamilies(self,n,reservedSeats):
        rows={}
        for r,s in reservedSeats:
            rows[r]=rows.get(r,0)|(1<<s)
        ans=(n-len(rows))*2
        for mask in rows.values():
            left=all(not(mask&(1<<s)) for s in range(2,6))
            mid=all(not(mask&(1<<s)) for s in range(4,8))
            right=all(not(mask&(1<<s)) for s in range(6,10))
            if left and right:
                ans+=2
            elif left or mid or right:
                ans+=1
        return ans