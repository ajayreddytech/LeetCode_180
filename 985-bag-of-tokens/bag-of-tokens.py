class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:

        # first we sort the tokens in ascending order
        # smaller tokens are good to play FU, larger tokens are good to play FD
        tokens.sort()  

        # set two pointers and initial score
        p1 = 0            # start pointer for smallest token
        p2 = len(tokens)-1 # end pointer for largest token
        score = 0
        max_score = 0     # we always keep track of max score at all times
        
        # start the while loop like usual pointer problems
        while p1 <= p2:
            token = tokens[p1]

            # if we have enough power, play FU
            if power >= token:
                power -= token     # lose power
                score += 1         # gain score
                max_score = max(score, max_score)  # update max score
                p1 += 1            # move left pointer forward

            else:
                # if not enough power, try FD with largest token
                token = tokens[p2]
                if score > 0:      # can only play FD if we have score
                    power += token # gain power
                    score -= 1     # lose score
                    p2 -= 1        # move right pointer backward 
                    # and continue the while loop with the same p1 where we left off
                else:
                    # cannot play FU or FD, game over
                    return max_score

        # return the max score we could get
        return max_score
