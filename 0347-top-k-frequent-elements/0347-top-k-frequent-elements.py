from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            buckets[freq].append(num)
        
        result = []

        for i in range(len(buckets)-1, -1, -1):
            for num in buckets[i]:
                result.append(num)

                if len(result) == k:
                    return result


        # Time Complexity: O(n), Space Complexity: O(n)

                
            






        
        