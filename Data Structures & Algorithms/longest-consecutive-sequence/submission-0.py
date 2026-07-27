class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        
        for num in num_set:
            # 1. Check if 'num' is the START of a sequence (i.e. num - 1 is NOT in set)
            if (num - 1) not in num_set:
                length = 1
                
                # 2. While the NEXT consecutive number (num + length) IS in the set...
                while (num + length) in num_set:
                    length += 1
                
                # 3. Update longest streak found so far
                longest = max(longest, length)
                
        return longest