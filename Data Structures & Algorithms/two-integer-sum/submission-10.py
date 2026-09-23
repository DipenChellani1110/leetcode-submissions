class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, n in enumerate(nums):
            x = target - n
            if x in hashmap:
                return [hashmap[x], i]
            hashmap[n] = i
