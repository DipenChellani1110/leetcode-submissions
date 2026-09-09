class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # make sure both the strings are of same length
        if len(s) != len(t):
            return False
        
        # create hashmap
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        # compare count of each character in both the strings

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        
        return True