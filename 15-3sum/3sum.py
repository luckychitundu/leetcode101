class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(0, len(nums)-2):
            l, r = i + 1, len(nums) - 1 
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    res.add(tuple([nums[i], nums[l], nums[r]])) 
                    l +=1 
                    r -= 1 
                elif  nums[i] + nums[l] + nums[r] < 0:
                    l += 1 
                else:
                    r -= 1 
        return res             

        