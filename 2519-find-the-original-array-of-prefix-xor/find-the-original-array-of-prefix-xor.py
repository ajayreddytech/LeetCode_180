# if u write down on paper, the whole pref-array, each and every ele, interms of arr-arrays
# u gonna figure out
# a0 = p0
# a1 = p1 ^ p0
# a2 = p2 ^ p1
# a3 = p3 ^ p2
# so, a(n) = p(n) ^ p(n-1)
# why? self cancelling prop of XOR

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:

        # initializing the arr - array
        arr = [0] * len(pref)

        # so loop and apply the formula: a(n) = p(n) ^ p(n-1)
        # except for i=0, special case
        for i in range(len(pref)):
            if i == 0:
                arr[i] = pref[i]
            else:
                arr[i] = pref[i] ^ pref[i-1]
        
        return arr