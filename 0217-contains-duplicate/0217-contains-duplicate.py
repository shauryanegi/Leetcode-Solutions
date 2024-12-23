class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # O(n) Time and Space Complexity
        hashset = set()

        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False        