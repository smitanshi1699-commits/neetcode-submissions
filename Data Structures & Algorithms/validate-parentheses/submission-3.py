class Solution:
    def isValid(self, s: str) -> bool:
        a = list(s)
        my_stack= []
        print(a[0])
        print(a)
        if a[0] == ')' or a[0] == '}' or a[0] == ']':
            return False
        for i in a:
            if i == ')':
                if len(my_stack) > 0 and '(' == my_stack[-1]:
                    my_stack.pop()
                else:
                    return False
            elif i == '}':
                if len(my_stack) > 0 and '{' == my_stack[-1]:
                    my_stack.pop()
                else:
                    return False
            elif i == ']':
                if len(my_stack) > 0 and '[' == my_stack[-1]:
                    my_stack.pop()
                else:
                    return False
            else :
                my_stack.append(i)
        if len(my_stack) == 0:
            return True
        else:
            return False



# if a[n] == ')':
#     if '(' in stack:
#         stack.remove('(')
# elif a[n] == ']':
#     if '[' in stack:
#         stack.remove('[')
# elif a[n] == '}':
#     if '{' in stack:
#         stack.remove('{')
# else:
#     stack.append(a[n])

# if stack.is_empty()