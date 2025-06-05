class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        i = 0

        # Using a list instead of string concatenation for efficiency.
        # In Python, strings are immutable â every s += c creates a new string,
        # leading to O(n^2) time in the worst case. List append is O(1) amortized,
        # and ''.join(res) at the end is linear, making the whole process O(n + m).
        while i < min(len(word1), len(word2)):
            res.append(word1[i])
            res.append(word2[i])
            i += 1

        if i < len(word1):
            res.append(word1[i:])

        if i < len(word2):
            res.append(word2[i:])

        return "".join(res)

        # Time Complexity: O(n + m)
        # Space Complexity: O(n + m)
