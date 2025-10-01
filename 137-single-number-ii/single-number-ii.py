class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in range(32):
            sum = 0
            for num in nums:
                if(num & (1 << i)):
                    sum += 1 #? why adding 1 and not the bit
            if (sum % 3 == 1):
                result |= (1 << i)

         # handle negative numbers
        if result >= 2**31:
            result -= 2**32
        return result