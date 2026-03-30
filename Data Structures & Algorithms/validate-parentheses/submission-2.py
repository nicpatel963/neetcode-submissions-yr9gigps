class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
           match i:
            case ')':
                if len(stack) !=0 and stack.pop() == '(':
                    continue
                else:
                    return False
            case '}':
                if len(stack) !=0 and stack.pop() == '{':
                    continue
                else:
                    return False
            case ']':
                if len(stack) !=0 and stack.pop() == '[':
                    continue
                else:
                    return False
            case _:
                stack.append(i)
        if len(stack) != 0:
            return False
        return True

