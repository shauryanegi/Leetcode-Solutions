class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        for i in range(len(strs[0])): # Only first string
            for s in strs: 
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]

        return strs[0]

        # Time complexity: O(nâm)
        # Space complexity: O(1) since we did not use extra space