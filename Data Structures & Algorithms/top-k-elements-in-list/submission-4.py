class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        list1 = []
        list2 = []
        for i in nums:
            hashmap[i] = hashmap.get(i,0) + 1
        for i in range(len(nums)+1):
            list1.append([])
        for num,freq in hashmap.items():
            list1[freq].append(num)
        for i in range(len(nums) , 0, -1):
            for num in list1[i]:
                list2.append(num)
                if len(list2) == k:
                    return list2



