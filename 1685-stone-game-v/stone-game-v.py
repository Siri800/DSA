from functools import cache
from itertools import accumulate
class Solution:
    def stoneGameV(self,stoneValue):
        prefix=list(accumulate(stoneValue,initial=0))
        @cache
        def dfs(left,right):
            if left>=right:
                return 0
            answer=0
            leftSum=0
            rightSum=prefix[right+1]-prefix[left]
            for middle in range(left,right):
                leftSum+=stoneValue[middle]
                rightSum-=stoneValue[middle]
                if leftSum<rightSum:
                    if answer>=leftSum*2:
                        continue
                    answer=max(answer,leftSum+dfs(left,middle))
                elif leftSum>rightSum:
                    if answer>=rightSum*2:
                        break
                    answer=max(answer,rightSum+dfs(middle+1,right))
                else:
                    answer=max(answer,leftSum+dfs(left,middle),rightSum+dfs(middle+1,right))
            return answer
        return dfs(0,len(stoneValue)-1)