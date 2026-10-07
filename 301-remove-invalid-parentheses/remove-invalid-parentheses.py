class Solution:
    def removeInvalidParentheses(self,s):
        def valid(x):
            count=0
            for c in x:
                if c=="(":
                    count+=1
                elif c==")":
                    count-=1
                    if count<0:
                        return False
            return count==0
        level={s}
        while True:
            ans=[x for x in level if valid(x)]
            if ans:
                return ans
            next_level=set()
            for x in level:
                for i in range(len(x)):
                    if x[i] in "()":
                        next_level.add(x[:i]+x[i+1:])
            level=next_level