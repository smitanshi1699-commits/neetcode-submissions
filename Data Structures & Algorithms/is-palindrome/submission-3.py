class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^A-Za-z0-9]','',s).lower()
        b = len(s)
        #print(new_s)
        for i in range(0,b//2):
            #print(i,b-1-i)
            #print (new_s[i] , new_s[b-1-i])
            if s[i] != s[b-1-i]:
                return False
        return True