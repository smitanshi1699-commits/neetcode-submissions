class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            a={}
            b={}
            for i in s:
                if i in a.keys():
                    a[i]+=1
                    print(i, a[i])
                else:
                    a[i] =1
            for i in t:
                if i in b.keys():
                    b[i]+=1
                else:
                    b[i] =1
            print(a,b)
            return a==b
        return False