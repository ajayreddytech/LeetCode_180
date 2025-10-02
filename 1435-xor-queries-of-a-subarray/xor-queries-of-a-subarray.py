class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:

        # we need to compute the prefix-array from the original-array
        # once we have the prefix-array, we can compute any XORs in any range in the original-array, easily using the formula
        # the formula is, if a<b, XORs of all eles in the original-array from a to b is P(a-1) ^ P(b)
        # why, since b is greater, P(b) already has P(a) in it, but XORing with P(a-1),
        # we get rid of the P(a-1) and we just P[a,b]
        # also, just a minor tweak, if a is 0, then the formula is P[a,b] is P(b)

        # initialize the prefix array
        prefixArray = [0] * len(arr)
        runningPrefix = 0

        # computing and filling the prefixArray
        for i in range(len(arr)):
            prefixArray[i] = runningPrefix ^ arr[i]
            runningPrefix = prefixArray[i]

        # initializing the answer array
        answer = [0] * len(queries)

        # computing and filling the answer array, using the formula
        for q in range(len(queries)):
            [a, b] = queries[q]

            if a == 0:
                answer[q] = prefixArray[b]
            else:
                answer[q] = prefixArray[a-1] ^ prefixArray[b]
        
        # finally return the answer array
        return answer

