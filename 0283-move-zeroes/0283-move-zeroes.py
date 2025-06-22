class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def swap(i,j):
            nums[i], nums[j] = nums[j], nums[i]

        j = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                swap(i, j)
                j += 1
        
        # TC: O(N)
        # SC: O(1)
        