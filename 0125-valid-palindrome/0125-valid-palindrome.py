class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Time Complexity: O(n)
            - We scan each character at most once from both ends (left and right pointers).
        
        Space Complexity: O(1)
            - No extra space used for data structures.
            - We only use pointers and temporary variables (constant space).
        """
        l = 0
        r = len(s) - 1

        while l < r:
            if not s[l].isalnum():
                l += 1
                continue

            if not s[r].isalnum():
                r -= 1
                continue

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True
