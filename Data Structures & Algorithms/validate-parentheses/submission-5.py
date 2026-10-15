class Solution:
    def isValid(self, s: str) -> bool:
        a = list(s)
        my_stake = []
        if a[0] == "]" or a[0] == "}" or a[0] == ")":
            return False
        
        for i in a :
            if i ==")":
                if len(my_stake) > 0 and my_stake[-1] == "(":
                    my_stake.pop()
                else:
                    return False
            elif i =="}":
                if len(my_stake) > 0 and my_stake[-1] == "{":
                    my_stake.pop()
                else:
                    return False
            elif i =="]":
                if len(my_stake) > 0 and my_stake[-1] == "[":
                    my_stake.pop()
                else:
                    return False
            else:
                my_stake.append(i)
        if len(my_stake) == 0:
            return True
        else:
            return False
                