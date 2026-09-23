class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # a - z -> 26
        # count [a-z] use hashmap -  key:[eat, tea ...]
        # T: O(m*n*26)

        res = defaultdict(list) # mapping char count to list of anagrams

        for s in strs:
            count = [0] * 26 # a to z

            for c in s:
                count[ord(c) - ord("a")] += 1
            
            res[tuple(count)].append(s)  #list cannot be keys
        
        return list(res.values())
