class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        tokens.sort()
        while len(tokens) != 0:
            canfaceup = True
            if tokens[0] <= power:
                score += 1
                power -= tokens.pop(0)
            else:
                canfaceup = False
            
            if (not canfaceup):
                if len(tokens) >= 3 and score >= 1:
                    score -= 1
                    power += tokens.pop(-1)
                else:
                    break
            
                
        return score