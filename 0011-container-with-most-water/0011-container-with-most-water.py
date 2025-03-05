class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        minheight = 0
        area = 0
        while left < right:
            minheight = min(height[left], height[right])
            area = max(area, minheight * (right - left))

            if height[left] < height[right]:
                left += 1
            else: 
                right -=1
        
        return area