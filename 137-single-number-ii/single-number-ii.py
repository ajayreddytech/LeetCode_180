class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # this is the result which we gonna return at the end
        # currently inid as zero, but we gonna change it bit by bit to get the actual no.
        result = 0

        # 32 iterations - why 32? 
        # coz we all know computer stores everything as binary internally
        # but how many bits in each of those binary nums - answer is 32 
        # also leetcode problem statement says, each num is stored in 32 bits
        for i in range(32):

            # we need this to compute the sum of all the bits at bit-pos-i
            sum = 0

            # iterating through all the nums and computing the sum of all bits at bit-pos-i in all nums
            for num in nums:
                sum += (num >> i) & 1
            
            # once sum is computed, we gonna do modulo 3, since binary, we gonna get either 0 or 1 as the result
            # if it is zero, we need not change the bit in result at bit-pos-i, since it is already 0
            # if it is one, we just change the bit in result at bit-pos-i to one
            if (sum % 3 == 1):
                result = (1 << i) | result

        # handle negative numbers
        # if the result is greater than the largest possible +ve number (given in the leetcode problem description)
        # then just wrap around by subtracting 2**32
        if result > 2**31 - 1:
            result = result - 2**32

        return result
