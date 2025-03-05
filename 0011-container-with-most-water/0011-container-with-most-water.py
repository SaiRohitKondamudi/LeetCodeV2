class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        area = 0
        minhei = 0
        while left < right:
            minhei = min(height[left], height[right])
            area = max(area, minhei * (right - left))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return area