class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Two Pointers 
        # Initialize left pointer at 0 and right pointer at n-1 
        # Update volume, and move pointer which has less height. 
        # Left pointer moves rightwards, right pointer moves leftwards 
        max_volume = 0  
        l, r = 0, len(height) - 1
        while l < r:
            h, w = min(height[l], height[r]), abs(l-r) 
            current_volume = h *  w 
            max_volume = max(max_volume, current_volume) 

            if height[l] < height[r]:
                l += 1 
            else:
                r -= 1 
        return max_volume             


