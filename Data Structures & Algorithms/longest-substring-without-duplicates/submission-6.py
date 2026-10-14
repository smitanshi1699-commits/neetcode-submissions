class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r = 0
        c = set()
        i = 0
        for j in range(len(s)):
            while s[j] in c:
                c.remove(s[i])
                i += 1
            c.add(s[j])
            r = max(r, j - i + 1)
        return r