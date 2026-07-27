class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        prefix_map = {0: 1} 

        for num in nums:
            current_sum += num
            
            # 1. Calculate the required old prefix sum (diff)
            diff = current_sum - k
            
            # 2. Add the number of times 'diff' has appeared in prefix_map to 'count'
            count += prefix_map.get(diff, 0)
            
            # 3. Store/update current_sum in prefix_map for future numbers
            prefix_map[current_sum] = 1 + prefix_map.get(current_sum, 0)
            
        return count