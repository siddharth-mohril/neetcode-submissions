class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        R = len(numbers) - 1
        L = 0 
        while R > L:
            add = numbers[R] + numbers[L] 
            if add == target:
                return [L+1,R+1]
            if add > target:
                R -= 1
            
            if add < target:
                L += 1




        