class Solution:
    def twoSum(self, nums, target):
        seen = {}                          # value -> index
        for i, n in enumerate(nums):
            need = target - n
            if need in seen:
                return [seen[need], i]
            else:
                seen[n] = i