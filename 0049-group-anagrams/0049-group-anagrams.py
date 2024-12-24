class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)

        # for s in strs:
        #     sortedS = ''.join(sorted(s))
        #     res[sortedS].append(s)

        # return list(res.values())

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            key = tuple(count)
            anagrams_dict[key].append(s)

        return list(anagrams_dict.values())

        # Time Complexity: O(m * n)
        # Space Complexity: O(m * n)
                