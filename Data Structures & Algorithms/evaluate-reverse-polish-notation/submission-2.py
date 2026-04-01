class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        for tok in tokens:
            if tok == '+':
                num2 = num_stack.pop()
                num1 = num_stack.pop()
                num_stack.append(num1 + num2)
            elif tok == '-':
                num2 = num_stack.pop()
                num1 = num_stack.pop()
                num_stack.append(num1 - num2)
            elif tok == '*':
                num_stack.append(num_stack.pop() * num_stack.pop())
            elif tok == '/':
                divisor = num_stack.pop()
                dividend = num_stack.pop()
                num_stack.append(int(float(dividend) / divisor))
            else:
                num_stack.append(int(tok))
            
        return num_stack[0]