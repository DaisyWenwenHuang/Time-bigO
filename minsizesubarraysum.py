# https://leetcode.com/problems/minimum-size-subarray-sum/
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0, 0
        minlen = float('infinity')
        
        for r in range(len(nums)):
            total = sum(nums[l:r + 1])
            while total >= target:
                minlen = min(minlen, (r - l + 1))
                l += 1
                total = sum(nums[l:r + 1])
        if minlen != float('infinity'):
            return minlen
        else:
            return 0

# better vision
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0, 0
        minlen = float('infinity')
        
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                minlen = min(minlen, (r - l + 1))
                total -= nums[l]
                l += 1
        if minlen != float('infinity'):
            return minlen
        else:
            return 0
        