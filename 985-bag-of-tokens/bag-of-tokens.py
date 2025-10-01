class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:

        # first lets sort the tokens in AO
        tokens.sort()  

        # set the pointers and score
        p1 = 0
        p2 = len(tokens)-1
        score = 0
        max_score = 0
        
        while(p1 <= p2):
            token = tokens[p1]
            if (power >= token):
                power -=  token
                score += 1
                max_score = max(score, max_score) # so we keep track of our max score at all times
                p1 += 1
            else:
                token = tokens[p2]
                if(score > 0):
                    power += token
                    score -= 1
                    p2 -= 1
                else:
                    return max_score
        return max_score
        