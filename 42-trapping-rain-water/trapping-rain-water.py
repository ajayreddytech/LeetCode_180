class Solution:
    def trap(self, height: List[int]) -> int:
        # say we are talking about the element @ index 2 in the height array
        # left_maxes[2] will give the left_max of that ele till that point, including that point
        # right_maxes[2] will give the right_max of that ele from that point, including that point
        # once we have both, we will just use the formula to compute trapped rain water at that specific index
        length = len(height)
        left_maxes = [0] * length
        right_maxes = [0] * length

        # initiliaze current_left_max as the first ele, 
        # start the loop, keep tracking the current_left_max and also fill left_maxes array
        current_left_max = height[0]
        for i in range(len(height)):
            left_maxes[i] = max(current_left_max, height[i])
            current_left_max = left_maxes[i]
        
        # initiliaze current_right_max as the last ele, 
        # start the loop from back, keep tracking the current_right_max and also fill right_maxes array
        current_right_max = height[len(height)-1]
        for i in range(len(height)-1, -1, -1):
            right_maxes[i] = max(current_right_max, height[i])
            current_right_max = right_maxes[i]

        # since i is from len-1 to 0, right_maxes is already getting filled from that-corner to 0
        # so no need to reverse the right_maxes array

        # once u have both array, loop again, find TRW and sum all them and return
        trapped_rain_water = 0
        for i in range(len(height)):
            trapped_rain_water += min(left_maxes[i], right_maxes[i]) - height[i]
        
        return trapped_rain_water