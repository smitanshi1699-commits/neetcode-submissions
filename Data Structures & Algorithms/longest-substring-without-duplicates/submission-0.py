class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r = 0
        for i in range (len(s)):
            c = set()
            for j in range (i,len(s)):
                if s[j] in c:
                    break
                c.add(s[j])
            r = max(r , len(c))
        return r