class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        li=[]
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    li.append(nums[i])
        return li
