class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS = {}
        countT = {}

        for ch_s, ch_t in zip(s, t):
            countS[ch_s] = 1 + countS.get(ch_s, 0)
            countT[ch_t] = 1 + countT.get(ch_t, 0)

        return countS == countT 

        # TC: O(n), SC: O(1) — constant alphabet size (26 lowercase letters)
