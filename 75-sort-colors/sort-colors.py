
# why did we inc current in case of 0 and not in case of 2?
# in 0's case, since we processed all eles before, we will mostly recieve 1 as the new ele, 
# so by incing current, am skipping that newly received one, and is totally fine

# but in case of swapping in case of 2
# we do not know what is the newly received ele
# so if i inc current, am just skipping that ele, without giving it its proper position
# so thats why no inc current incase of 2

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        current = 0 # to loop through the array using a while loop
        p0 = 0 # pointer to track the zeros
        p2 = len(nums)-1 # pointer to track the twos

        while(current <= p2):
            # do nothing if the current ele is one
            if nums[current] == 1:
                current += 1

            # if the current ele is 0, swap with the one at p0 and inc p0
            elif nums[current] == 0:
                [nums[current], nums[p0]] = [nums[p0], nums[current]]
                p0 += 1
                current += 1
            
            # if the current ele is 2, swap with the one at p2 and dec p2
            else:
                [nums[current], nums[p2]] = [nums[p2], nums[current]]
                p2 -= 1
                #current += 1

            