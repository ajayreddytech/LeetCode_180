class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 2 pointers, one at start and one at end
        p1 = 0
        p2 = len(height)-1

        # initialize area and max_area
        area = 0
        max_area = 0

        # while pointers don’t cross
        while(p1 < p2):
            # area formula = min height × distance
            # why min? coz water only goes till smaller height, and no slanting
            area = min(height[p1], height[p2]) * (p2 - p1)

            # keep track of the biggest area so far
            max_area = max(area, max_area)

            # now time to move pointers
            # whichever has smaller height, we move that, coz min height is the deciding factor
            if height[p1] < height[p2]:
                p1 += 1
            elif height[p2] < height[p1]:
                p2 -= 1
            else:
                # if both have equal heights, can move either
                p1 += 1

        # finally return the max_area we got
        return max_area
