class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        # these are the start and end of our sliding window
        # also initializing sum to keep track of sliding_window_sum
        # also initializing the counter that we need to return at the end
        start = 0
        end = start + k - 1
        sw_sum = sum(arr[start:end+1])
        counter = 1 if sw_sum >= threshold * k else 0

        # updating the start and end of the sliding window
        start += 1
        end = start + k - 1

        while(end < len(arr)):
            # updating sliding window sum
            sw_sum = sw_sum + arr[end] - arr[start-1]

            # updating the counter
            if sw_sum >= threshold * k:
                counter += 1
            
            # updating the start and end of the sliding window
            start += 1
            end = start + k - 1
            
        return counter





