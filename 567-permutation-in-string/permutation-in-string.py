class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1_hashmap = {}

        # hashmap for s1
        for i in range(len(s1)):
            s1_hashmap[s1[i]] = s1_hashmap.get(s1[i], 0) + 1
        
        sw = s2[0:len(s1)]
        sw_hashmap = {}

        # hashmap for sw
        for i in range(len(sw)):
            sw_hashmap[sw[i]] = sw_hashmap.get(sw[i], 0) + 1
        
        if(s1_hashmap == sw_hashmap):
            return True

        for i in range(1, len(s2)-len(s1)+1):

            # need not update sliding window each time, just updating hashmap is enough
            # also updating SW is O(n)

            sw_hashmap[s2[i+len(s1)-1]] = sw_hashmap.get(s2[i+len(s1)-1], 0) + 1
            sw_hashmap[s2[i-1]] = sw_hashmap.get(s2[i-1], 0) - 1

            if(sw_hashmap[s2[i-1]] <= 0):
                del sw_hashmap[s2[i-1]]
                    
            if(s1_hashmap == sw_hashmap):
                return True

        return False