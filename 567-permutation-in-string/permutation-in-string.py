class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # base case, if s1 is bigger than s2, no chance of permutation being present
        if len(s1) > len(s2):
            return False

        s1_hashmap = {}

        # hashmap for s1
        for i in range(len(s1)):
            s1_hashmap[s1[i]] = s1_hashmap.get(s1[i], 0) + 1
        
        sw = s2[0:len(s1)]
        sw_hashmap = {}

        # hashmap for sw (first window of size len(s1))
        for i in range(len(sw)):
            sw_hashmap[sw[i]] = sw_hashmap.get(sw[i], 0) + 1
        
        # check for the very first window itself
        if(s1_hashmap == sw_hashmap):
            return True

        # now slide the window one step at a time
        for i in range(1, len(s2)-len(s1)+1):

            # need not update the actual sw string each time, just updating hashmap is enough
            # updating sw string would be O(n), but hashmap update is O(1)

            e_add = i+len(s1)-1   # index of new ele that is getting added to sw/sw_hashmap
            e_remove = i-1        # index of ele that is getting removed from sw/sw_hashmap

            # add the new char into hashmap
            sw_hashmap[s2[e_add]] = sw_hashmap.get(s2[e_add], 0) + 1

            # decrement the count of the char going out
            sw_hashmap[s2[e_remove]] = sw_hashmap.get(s2[e_remove], 0) - 1

            # if count of some char becomes 0 or negative, remove it from hashmap
            # this ensures dict sizes stay minimal and clean
            if(sw_hashmap[s2[e_remove]] <= 0):
                del sw_hashmap[s2[e_remove]]
                    
            # after each update, check if the two hashmaps match
            # if they match, that means current sw is a permutation of s1
            if(s1_hashmap == sw_hashmap):
                return True

        # loop ends → no permutation found anywhere in s2
        return False
