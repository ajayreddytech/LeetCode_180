# 2 ways to do this problem
# one using arithmetic sum, since nums are distinct
# other using XOR property of pairs-getting-self-cancelled

# missing_number = arithmetic_sum - sum of array eles
# missing_number = xor of all eles in the array (xor) xor of all the nums from 0 to the length of the array

class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # initialize missing_number with 0, coz xor of a num with 0 is num
        missing_number = 0
        for i in range(len(nums)):

            # xor with i and nums[i]
            missing_number ^= i
            missing_number ^= nums[i]

        # one last number is left out, we will xor that as well
        missing_number ^= len(nums)
        return missing_number
