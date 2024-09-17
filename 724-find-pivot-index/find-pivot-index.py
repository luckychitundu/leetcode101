class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """
        [1,7,3,6,5,6]

        """
        # Visit every index,
        # Compute sum to the left, and sum to the right
        # Return index if sums are equal 
        for i in range(len(nums)):
            left_sum, right_sum = sum(nums[:i]), sum(nums[i+1:])
            if left_sum == right_sum:
                return i 
        return -1         

        