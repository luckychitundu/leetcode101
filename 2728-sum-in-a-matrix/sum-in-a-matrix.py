class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        # 7, 6, 6, 3 -> 7 
        # 2, 4, 5, 2 -> 5
        # 1, 2, 3, 1 -> 3 
        # 7 + 5 + 3 = 15  
        # Brute Force
        # Sort elements in each row in descending order 
        # nums = [[7,2,1],[6,4,2],[6,5,3],[3,2,1]] 
        # Hashmap to store each index with max value at that index
        # Return the sum of values of resulting hashmap 
        nums = [sorted(row, reverse=True) for row in nums] 
        print(nums)
        mapping = {}
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                if j not in mapping:
                    mapping[j] = nums[i][j] 
                else:
                    mapping[j] = max(mapping[j], nums[i][j])
        return sum(mapping.values())            

