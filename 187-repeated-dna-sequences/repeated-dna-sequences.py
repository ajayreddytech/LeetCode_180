# if no duplicates, return []

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10: return []

        sw = s[0:9+1]
        seen = set()
        repeated = set()

        seen.add(sw)

        for i in range(1, len(s)-10+1):
            sw = sw[1:] + s[i+9]
            if sw in seen:
                repeated.add(sw)
            else:
                seen.add(sw)
        
        return list(repeated)

