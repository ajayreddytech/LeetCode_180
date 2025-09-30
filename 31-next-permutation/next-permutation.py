class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # initiate dip to -1
        dip = -1


        # looping from the back
        # find the first number that is less than the current no. and is also next to the current no.
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] < nums[i]:
                dip = i-1 # this is the dip index
                break # and break, coz we need the loop, only till we find this dip
        

        # if the dip is still -1, that means there is no dip at all
        # which means all the nums are in descending order
        # and we just need to return them in ascending order
        # which is to reverse and return
        if dip == -1:
            nums.reverse()
            return


        # below code runs if we find a dip
        # looping back from len(nums)-1 to dip 
        # and finding the number that is greater than dip
        # once found, swap the dip and the found
        for j in range(len(nums)-1, dip, -1):
            if nums[j] > nums[dip]:
                nums[j], nums[dip] = nums[dip], nums[j]
                break # and break, coz we need the loop, only till we find the thing and swap


        # then reverse all the nums from dip+1 to the end
        # they call this part (dip+1 to end) the tail
        nums[dip+1:] = reversed(nums[dip+1:])