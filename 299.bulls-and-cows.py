class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull, cow = 0,0
        d1, d2 = {}, {}
        for i in range(len(guess)):
            if secret[i] == guess[i]:
                bull += 1
            else:
                if secret[i] in d1:
                    d1[secret[i]] += 1
                else:
                    d1[secret[i]] = 1
                if guess[i] in d2:
                    d2[guess[i]] += 1
                else:
                    d2[guess[i]] = 1
        for key in d1:
            if key in d2:
                cow += min(d1[key],d2[key])
        return str(bull)+"A"+str(cow)+"B"
