class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == [""]:
            return ""

        min_str = min(strs, key=len)

        for index, char in enumerate(min_str):
            for word in strs:
                if word[index] != char:
                    return min_str[:index]

        return min_str

            # Time Complexity: O(n * m), where n = number of strings, m = length of shortest string
            
        # Space Complexity: O(1)
