class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}  # Key: number, Value: index
        
        for i in range(len(nums)):
            current_number = nums[i]
            complement = target - current_number
            

            if complement in hashmap:
                return [hashmap[complement], i]
            

            hashmap[current_number] = i