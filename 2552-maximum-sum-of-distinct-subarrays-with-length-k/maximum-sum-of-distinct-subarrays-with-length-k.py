class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        # these are the start and end of our sliding window
        # also initializing sum and max_sum to keep track of sliding_window_sum and max_sum
        start = 0
        end = start + k - 1
        sw_sum = 0
        max_sum = 0

        # we gonna need a hashmap to store the frequencies of the nums in the sliding window
        hashmap = {}

        # storing the frequencies of the numbers inside the sliding window inside the hashmap
        for i in range(start, end+1):
            hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1

        # updating sliding_window_sum & max_sum
        # sum updates all the time, but max_sum updates only when len(hashmap) == k, for the sliding window
        sw_sum = sum(nums[start:end+1])
        max_sum = (max(sw_sum, max_sum)) if (len(hashmap) == k) else max_sum

        # updating start and end
        start += 1
        end = start + k - 1

        while(end <= len(nums)-1):
            # updating sliding_window_sum by removing and adding appropriate elements
            sw_sum = sw_sum + nums[end] - nums[start-1]

            # updating hashmap by adding and removing appropriate elements
            # if the value of the key is zero, after removing, we just delete the key from the hashmap
            hashmap[nums[end]] = hashmap.get(nums[end], 0) + 1
            hashmap[nums[start-1]] = hashmap.get(nums[start-1], 0) - 1
            if hashmap[nums[start-1]] <= 0:
                del hashmap[nums[start-1]]

            # max_sum updates only when len(hashmap) == k, for the sliding window
            max_sum = (max(sw_sum, max_sum)) if (len(hashmap) == k) else max_sum

            # updating start and end
            start += 1
            end = start + k - 1

        return max_sum