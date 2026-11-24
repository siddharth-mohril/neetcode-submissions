class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = []
        maxR = []
        maxLv = 0
        maxRv = 0
        water = 0

        for i in range(0,len(height)):
            if height[i] > maxLv:
                maxLv = height[i]
            maxL.append(maxLv)

        for i in range(len(height)-1,-1,-1):
            if height[i] > maxRv:
                maxRv = height[i]
            maxR.append(maxRv)
        
        maxR.reverse()
        
        for i in range(0,len(height)):
            minimum = min(maxL[i],maxR[i])
            water += (minimum-height[i])

        return water
