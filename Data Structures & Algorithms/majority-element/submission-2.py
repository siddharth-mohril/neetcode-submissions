class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = hashmap.get(nums[i],0) + 1
        bucket = []
        
        count = 0
        res = 0
        for i,j in hashmap.items() :
            if count < j:
                count = j
                res = i
        return res

        