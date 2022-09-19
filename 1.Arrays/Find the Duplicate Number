class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new_arr=[]
        l=len(nums)
        for i in nums[:]:
            if i==0:
                nums.remove(i)
                new_arr.append(i)
            
        nums.extend(new_arr)
                  
