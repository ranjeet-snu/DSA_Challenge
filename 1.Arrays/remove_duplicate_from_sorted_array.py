class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = len(nums)-1
        while temp > 0:
            if nums[temp] == nums[temp-1]:
                nums.pop(temp)
            temp = temp-1
