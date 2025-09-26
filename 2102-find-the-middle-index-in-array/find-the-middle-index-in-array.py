class Solution:
    # ajay
    def findMiddleIndex(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        leftSum = 0

        for i in range(len(nums)):
            rightSum = totalSum - leftSum - nums[i]
            if(leftSum == rightSum):
                return i
            leftSum = leftSum + nums[i]

        return -1



