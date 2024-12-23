class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Implements binary search to find the target value in a sorted array.
        Addresses potential integer overflow by modifying the mid calculation.

        Parameters:
        nums (List[int]): A list of integers sorted in ascending order.
        target (int): The value to search for.

        Returns:
        int: The index of the target if found, otherwise -1.

        Time Complexity:
        - Best Case: O(1) â The target is found at the first check.
        - Worst Case: O(log n) â The search space is halved in each iteration.
        - Average Case: O(log n).

        Space Complexity:
        - O(1) â The algorithm uses constant space with no additional data structures.

        Notes:
        - To prevent integer overflow, mid is calculated as:
          mid = left + (right - left) // 2
        - This avoids the potential overflow issue that can occur with:
          mid = (left + right) // 2
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2  # Prevents potential overflow
            # mid = (left + right) // 2
            
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid

        return -1
