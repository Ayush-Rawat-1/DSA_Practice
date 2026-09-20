class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        if all(i == 0 for i in nums):
            return 0
        curr=0
        for i in nums:
            curr ^= i
        
        return len(nums)-int(curr == 0)
