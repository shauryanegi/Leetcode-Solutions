class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0) # Count frequencies

        for num, cnt in count.items():
            freq[cnt].append(num) # Store numbers by frequency

        res = []
        for i in range(len(freq) -1, 0 , -1): # Iterate frequencies in reverse
            for num in freq[i]: # The total iterations of this inner loop across all outer loops is at most n
                res.append(num)

                if len(res) == k: # Return when k elements found
                    return res
        
    # Time complexity: O(n)
    # Space complexity: O(n)