# https://leetcode.com/problems/maximum-subarray/description/

class Solution:
    def maxSubArray(self, nums):
        max_curr = max_all = nums[0]
        for num in nums:
            max_curr = max(num, max_curr+num)
            max_all = max(max_curr, max_all)
        return max_all
