class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = re.sub(r'[^A-Za-z0-9]','',s).lower()
        a = True
        b = len(new_s)
        #print(new_s)
        for i in range(0,b//2):
            #print(i,b-1-i)
            #print (new_s[i] , new_s[b-1-i])
            if new_s[i] == new_s[b-1-i]:
                a = True
            else:
                a = False
        return a