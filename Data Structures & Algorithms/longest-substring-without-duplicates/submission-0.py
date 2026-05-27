class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        prev = {} 
        start = 0
        maxLength = 0
        for i in range(len(s)):
            if s[i] in prev and prev[s[i]] >= start:
                start = prev[s[i]] + 1
            prev[s[i]] = i
            length = i - start + 1
            if length > maxLength:
                maxLength = length
            
        return maxLength
