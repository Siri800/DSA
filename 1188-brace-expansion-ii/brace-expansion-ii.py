class Solution:
 def braceExpansionII(self,expression):
  def parse(i):
   res={""}
   total=set()
   while i<len(expression) and expression[i]!='}':
    if expression[i]==',':
     total|=res
     res={""}
     i+=1
    elif expression[i]=='{':
     cur,i=parse(i+1)
     res={a+b for a in res for b in cur}
    else:
     res={a+expression[i] for a in res}
     i+=1
   total|=res
   return total,i+1
  return sorted(parse(0)[0])


