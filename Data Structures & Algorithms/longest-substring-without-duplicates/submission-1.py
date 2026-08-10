class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        L = 0
        max_len = 0
        
        for R in range(len(s)):
            # 1. Duplicate mila? Toh Left se nikalo!
            while s[R] in char_set:
                char_set.remove(s[L])  # <--- BLANK 1: s[L] ko nikalo
                L += 1                 # Left pointer aage badhao
                
            # 2. Ab naye character ko party mein add karo
            char_set.add(s[R])         # <--- BLANK 2: s[R] ko add karo
            
            # 3. Current window size = (R - L + 1)
            max_len = max(max_len, R - L + 1)  # <--- BLANK 3: R - L + 1
            
        return max_len
        