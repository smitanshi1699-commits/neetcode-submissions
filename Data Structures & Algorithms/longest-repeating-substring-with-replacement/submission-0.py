class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        longest_substring = 0
        left =0
        max_frequency = 0

        for right in range(len(s)):
            char = s[right]
            count[char] = count.get(char,0) +1
            max_frequency = max(max_frequency,count[char])

            window_length = right - left + 1

            if window_length - max_frequency > k:
                left_char = s[left]
                count[left_char] -= 1
                left += 1
            
            longest_substring = max(longest_substring,right - left +1)
        
        return longest_substring