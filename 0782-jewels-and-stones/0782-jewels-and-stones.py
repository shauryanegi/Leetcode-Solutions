from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0

        jewels_set = set(jewels)
        # stones_counter = Counter(stones)
        
        # for stone,freq in stones_counter.items():
        #     if stone in jewels_set:
        #         ans += freq

        for stone in stones:
            if stone in jewels_set:
                ans += 1
        return ans