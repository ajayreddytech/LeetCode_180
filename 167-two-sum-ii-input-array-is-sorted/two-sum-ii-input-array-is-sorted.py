# one-indexed means the array is the same, 
# just the output they want in the one idexed fashion

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0 #pointer1
        p2 = len(numbers)-1 ##pointer2

        # why not p1 <= p2:
        # coz it is said, You may not use the same element twice.
        while p1 < p2:

            # why not use sum, why use tsum?
            # using sum shadows the inbuilt sum functionality of python
            tsum = numbers[p1] + numbers[p2]
            if tsum == target:
                return [p1+1, p2+1]
            elif tsum > target:
                p2 -= 1
            else:
                p1 += 1
        return []
