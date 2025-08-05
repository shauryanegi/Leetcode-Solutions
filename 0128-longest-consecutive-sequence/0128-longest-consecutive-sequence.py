class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # TC: O(n), SC: O(n) — set for O(1) lookups; each number visited once
        num_set = set(nums)
        max_len = 0

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                length = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    length += 1


                max_len = max(length, max_len)

        return max_len
