class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        bracket_map={')':'(',']':'[','}':'{'}
        for character in s:
            if character in '([{':
                stack.append(character)
            else:
                if not stack:
                    return False
                top=stack.pop()
                if top!=bracket_map[character]:
                    return False
        return len(stack)==0
                