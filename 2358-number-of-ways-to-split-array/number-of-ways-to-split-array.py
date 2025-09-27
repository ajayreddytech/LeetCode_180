class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        count = 0

        # assume
        lsum = 0
        rsum = sum(nums)

        for i in range(len(nums)-1):
            lsum += nums[i]
            rsum -= nums[i]

            # if the condition is equals then just put here ==
            # if the condition is >= then just put here >=
            # if the condition is < then just put here <
            # so whatever is the condition, just put it here
            if(lsum >= rsum):
                count += 1
        return count   