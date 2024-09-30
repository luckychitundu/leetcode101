class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(set(nums))
        n = len(nums)
        max_count = 0
        current_count = 1
        for i in range(1, n):
            if nums[i] == nums[i-1] + 1:
                current_count += 1 
                max_count = max(max_count, current_count) 
            else:
                current_count = 1 
        return max(max_count, current_count)          

