class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = high

        while low <= high:
            mid = (low + high) // 2

            hours = sum((math.ceil(p/mid) for p in piles))

            if hours <= h:
                ans = mid
                high = mid - 1
            
            else:
                low = mid + 1

        return ans

        # TC = O(log n)
        # SC = O(1)