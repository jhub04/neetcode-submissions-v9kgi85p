class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        final = 0

        while r > l:
            area = min(heights[l], heights[r]) * (r - l)
            if area > final:
                final = area
            
            if heights[l] >= heights[r]:
                r -= 1
            if heights[r] > heights[l]:
                l += 1

        return final

