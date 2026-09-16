class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        # frquency of chars we need and frequency of chars in current window
        countT, window = {},  {}

        # cound freq of each chars in t
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        # have = number of required chars whose freq is satisfied
        # need = number of unique chars we need to satify
        have, need = 0, len(countT)

        # store best window indices and its length
        res = [-1, -1]
        resLen = float("infinity")

        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            # check if the char's requried freq is satisfied?
            if c in countT and window[c] == countT[c]:
                have += 1
            
            # shrink from left if the window is valid
            while have == need:
                # update result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                # remove left char
                window[s[l]] -= 1

                # if removing left char makes the window invalid

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
            
                l += 1

        #return smallest window
        l, r = res
        return s[l:r + 1] if resLen != float("infinity") else ""         