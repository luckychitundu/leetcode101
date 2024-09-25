class Solution:
    # Initialize count 
    # Create gcd(x, y) function 
    # Nested loop to get all possible pairs in nums 
    # Increment count if given pair is beautiful i.e gcd(x, y) == 1

    def gcd(self, x, y):
        if x > y:
            small = y 
        else:
            small = x 
        for i in range(1, small + 1):
            if (x % i == 0) and (y % i == 0):
                gcd = i 
        return gcd                 

    def countBeautifulPairs(self, nums: List[int]) -> int:
        count = 0 
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                d1, d2 = int(str(nums[i])[0]), int(str(nums[j])[-1])
                print(f"d1: {d1}")
                print(f"d2: {d2}")
                if self.gcd(d1, d2) == 1:
                    count += 1 
        return count             

        