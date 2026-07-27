class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        count = 0
        res = 0
        for i in range(len(nums)):
            hashmap[nums[i]] = hashmap.get(nums[i],0) + 1
        target = len(nums) // 2
        for number,frequency in hashmap.items():
            if frequency > target :
                return number
