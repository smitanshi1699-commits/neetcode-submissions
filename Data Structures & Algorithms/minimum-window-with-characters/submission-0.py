class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(t)>len(s):
            return ""
        
        countT = Counter(t)
        window = {}

        have , need = 0 , len(countT)

        best_window = [-1,-1]
        min_length = float("inf")

        left = 0

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c,0) + 1

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                current_window = right - left +1
                if current_window < min_length:
                    best_window = [left,right]
                    min_length = current_window

                left_char = s[left]
                window[left_char] -= 1

                if left_char in countT and window[left_char] < countT[left_char]:
                    have -= 1
                    
                left += 1

        start, end = best_window
        return s[start : end + 1] if min_length != float("infinity") else ""
                