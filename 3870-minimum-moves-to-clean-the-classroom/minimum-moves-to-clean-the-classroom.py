from collections import deque
class Solution:
    def minMoves(self,classroom,energy):
        m=len(classroom)
        n=len(classroom[0])
        litter={}
        start=(0,0)
        for i in range(m):
            for j in range(n):
                if classroom[i][j]=='S':
                    start=(i,j)
                elif classroom[i][j]=='L':
                    litter[(i,j)]=len(litter)
        total=len(litter)
        if total==0:
            return 0
        target=(1<<total)-1
        q=deque()
        q.append((start[0],start[1],energy,0,0))
        seen=set()
        seen.add((start[0],start[1],energy,0))
        directions=((1,0),(-1,0),(0,1),(0,-1))
        while q:
            r,c,e,mask,d=q.popleft()
            if mask==target:
                return d
            if e==0:
                continue
            for dr,dc in directions:
                nr=r+dr
                nc=c+dc
                if nr<0 or nr>=m or nc<0 or nc>=n:
                    continue
                if classroom[nr][nc]=='X':
                    continue
                ne=e-1
                nm=mask
                if (nr,nc) in litter:
                    nm|=1<<litter[(nr,nc)]
                if classroom[nr][nc]=='R':
                    ne=energy
                state=(nr,nc,ne,nm)
                if state in seen:
                    continue
                seen.add(state)
                q.append((nr,nc,ne,nm,d+1))
        return -1