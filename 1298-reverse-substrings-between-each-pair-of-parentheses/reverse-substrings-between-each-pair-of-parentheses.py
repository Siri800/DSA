class Solution:
 def reverseParentheses(self,s):
  stack=[]
  for c in s:
   if c=='(':
    stack.append([])
   elif c==')':
    x=stack.pop()[::-1]
    if stack:
     stack[-1].extend(x)
    else:
     stack.append(x)
   else:
    if stack:
     stack[-1].append(c)
    else:
     stack.append([c])
  return ''.join(stack[0])
