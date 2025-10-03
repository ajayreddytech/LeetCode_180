# if no duplicates, return []
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # first, check if the string length <= 10, if yes return empty array
        if len(s) <= 10: return []

        # make our first sliding window (first 10 chars)
        sw = s[0:9+1]

        # make our 2 sets - seen and repeated
        seen = set()
        repeated = set()

        # add first window to seen
        seen.add(sw)

        # loop through the string to move the sliding window
        for i in range(1, len(s)-10+1):
            # tweak sliding window: remove first char, add next char from main string
            sw = sw[1:] + s[i+9]
            
            # check if current window is already in seen
            if sw in seen:
                # if yes, add to repeated
                repeated.add(sw)
            else:
                # if not, add to seen
                seen.add(sw)
        
        # finally convert repeated set to list and return
        return list(repeated)
