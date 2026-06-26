class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in {"+","-","*","/"}:
                right_num = stack.pop()
                left_num = stack.pop()

                if token == "+":
                    stack.append(left_num + right_num)
                elif token == "-":
                    stack.append(left_num - right_num)
                elif token == "*":
                    stack.append(left_num * right_num)
                elif token == "/":
                    stack.append(int(left_num / right_num))

            else:
                stack.append(int(token))
        return stack[0]