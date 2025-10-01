class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1 = 0
        p2 = len(height)-1
        area = 0
        max_area = 0


        while(p1 < p2):
            area = min(height[p1], height[p2])*(p2-p1)
            max_area = max(area, max_area)

            if height[p1] < height[p2]:
                p1 +=1
            elif height[p2] < height[p1]:
                p2 -= 1
            else:
                p1 +=1
        return max_area