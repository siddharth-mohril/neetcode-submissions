class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
            
        L = 0
        R = len(height) - 1
        left_max = height[L]
        right_max = height[R]
        res = 0
        
        while L < R:
            if left_max < right_max:
                L += 1
                left_max = max(left_max, height[L])
                res += left_max - height[L]
            else:
                R -= 1
                right_max = max(right_max, height[R])
                res += right_max - height[R]
                
        return res