# Algorithm (One Pass)

# Initialize:

# max_prod = nums[0]
# min_prod = nums[0]
# result = nums[0]

# Iterate from index 1 to end:
# If current number is negative, swap max_prod and min_prod
# Update max_prod = max(num, num * max_prod)
# Update min_prod = min(num, num * min_prod)
# Update result = max(result, max_prod)

# Return result

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        min_product = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            if num < 0:
                [max_product, min_product] = [min_product, max_product]
            max_product = max(num, max_product*num)
            min_product = min(num, min_product*num)
            result = max(result, max_product)
        return result