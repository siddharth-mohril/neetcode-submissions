class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        L = 0
        max_len = 0
        
        for R in range(len(s)):
            # 1. While there is a duplicate char in char_set...
            while s[R] in char_set:
                # Remove s[L] and shrink window
                char_set.remove(s[L])
                L += 1
                
            # 2. Add current character to char_set
            char_set.add(s[R])
            
            # 3. Update max length found so far (window size = R - L + 1)
            max_len = max(max_len, R-L+1)
            
        return max_len