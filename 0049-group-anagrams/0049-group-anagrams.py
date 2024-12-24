class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)

        # for s in strs:
        #     sortedS = ''.join(sorted(s))
        #     res[sortedS].append(s)

        # return list(res.values())

        for string in strs:
            count = [0] * 26

            for char in string:
                count[ord(char) - ord('a')] += 1

            keys = tuple(count)
            anagrams_dict[keys].append(string)
        return list(anagrams_dict.values())

        # Time Complexity: O(m * n)
        # Space Complexity: O(m * n)
                