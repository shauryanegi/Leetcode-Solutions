class Solution:
    def dominantIndex(self, nums: List[int]) -> int:

        if not nums:
            return -1

        max_val = -1
        second_max_val = -1
        max_index = -1
        
        for i, num in enumerate(nums):
            if num > max_val:
                second_max_val = max_val
                max_val = num
                max_index = i
            elif num > second_max_val:
                second_max_val = num

        if max_val >= 2 * second_max_val:
            return max_index

        else:
            return -1


        # Time Complexity: O(n), Space Complexity: O(1).