class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]: 
        seen = set()
        nums.sort() 
        for i in range(len(nums)): 
            left = i+1 
            right = len(nums)-1
            while left < right: 
                total = nums[i] + nums[left] + nums[right] 
                if total == 0: 
                    triplet = tuple([nums[i],nums[left],nums[right]])
                    seen.add(triplet) 
                    left += 1
                    right -= 1 
                elif total < 0:
                    left += 1 
                else: 
                    right -= 1 
        return [list(t) for t in seen]