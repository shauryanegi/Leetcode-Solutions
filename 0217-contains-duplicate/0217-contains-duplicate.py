class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Determines if the input list contains any duplicates.

        Approach:
        - Utilizes a hash set to track seen numbers. If a number is encountered that 
          already exists in the set, the function returns True.
        - If no duplicates are found, returns False.

        Parameters:
        nums (List[int]): A list of integers.

        Returns:
        bool: True if any value appears at least twice, otherwise False.

        Time Complexity:
        - O(n) â Iterates through the list once. 
        - Insertion and lookup operations in a hash set are O(1) on average.

        Space Complexity:
        - O(n) â A hash set is used to store up to n elements in the worst case.
        """
        hashset = set()

        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False
