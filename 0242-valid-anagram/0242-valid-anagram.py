class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        """
Time Complexity: O(n) - where n is the length of the strings s and t, as we iterate through each string once to count character frequencies.

Space Complexity: O(k) - where k is the number of unique characters in the strings, representing the space used to store the character counts in the dictionaries (worst case is O(n) if all characters are unique).
        """

        # return Counter(s) == Counter(t)
        
        if len(s) != len(t):
            return False
        #return sorted(s) == sorted(t)
        
        countS = {}
        countT = {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT
