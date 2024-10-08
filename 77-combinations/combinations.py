class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 1,2,3,4
        result = []
        
        # Helper function for backtracking
        def backtrack(start, current_combination):
            # If the current combination is of size k, add it to the result
            if len(current_combination) == k:
                result.append(current_combination[:])
                return
            
            # Explore further numbers starting from 'start'
            for i in range(start, n + 1):
                current_combination.append(i)
                backtrack(i + 1, current_combination)
                current_combination.pop()  # Backtrack, remove the last added number
        
        backtrack(1, [])
        return result