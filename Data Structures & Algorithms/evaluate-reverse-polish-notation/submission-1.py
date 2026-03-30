class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        for i in tokens:
            match i:
                case "+":
                    stack.append(stack.pop() + stack.pop())
                case "-":
                    b, a = stack.pop(), stack.pop()
                    stack.append(a - b)
                case "*":
                    stack.append(stack.pop() * stack.pop())
                case "/":
                    b, a = stack.pop(), stack.pop()
                    stack.append(int(a / b))
                case _:
                    stack.append(int(i))
        return stack[0]