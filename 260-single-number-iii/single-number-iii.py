class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:

        # inid as zero, (as xor of a num with 0 is num)
        # but we gonna get the xor of those 2 nums stored in here
        result = 0

        # computing the xor of all nums in the array
        for i in range(len(nums)):
            result ^= nums[i]

        # now, result stores xor of those 2 nums

        # to get the right most set-bit in the result
        # now the result has only one set-bit somewhere and all the other bits are zeroes
        result = result & -result

        # this result is gonna help us split the array into 2 parts
        # based on the result that we get, by ANDing the num with the result
        # we gonna xor those two parts seperately
        # since other nums are in pairs, XORing cancels them out and ultimately, only those 2 nums remain

        # inid as zeroes, (as xor of a num with 0 is num)
        # but we gonna get those 2 nums here, one in num1 and the other in num2
        num1 = 0
        num2 = 0

        for i in range(len(nums)):

            # AND each num with result
            # if >= 1, xor with one
            # if 0, xor with the other
            if(nums[i] & result):
                num1 ^= nums[i]
            else:
                num2 ^= nums[i]

        # since pairs cancel out after XORing, finally ony those two nums remain
        return [num1, num2]
