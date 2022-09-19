class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in nums:
            j=i+1
            if i in nums[j:]:
                return i
                  
