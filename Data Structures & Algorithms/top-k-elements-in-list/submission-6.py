class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # array -> nums, integer -> k 
        # return k most frequent elements 
        # [1, 2, 2, 3, 3, 3], k = 2
        # output: [2, 3]

        # create frequency map

        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        # for length n of "nums" - no number can occur more than n times so we create buckets where the index represents frquency
        # index:  0,   1,     2,   3
        # bucket: [], [1], [2], [3]

        freq = [[] for _ in range(len(nums) + 1)]

        for num, cnt in count.items():
            freq[cnt].append(num)
        
        result = []

        for cnt in range(len(freq) - 1, 0, -1):
            for num in freq[cnt]:
                result.append(num)

                if len(result) == k:
                    return result
