class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        openP = ['(','{','[']
        closeP = [')','}',']']

        for p in s:
            if p in openP:
                stack.append(p)
                continue

            if not stack:
                return False
            
            if p == ')' and stack[-1] == '(':
                stack.pop()
                continue
            
            if p == '}' and stack[-1] == '{':
                stack.pop()
                continue
                
            if p == ']' and stack[-1] == '[':
                stack.pop()
                continue

            return False

        return False if stack else True



        