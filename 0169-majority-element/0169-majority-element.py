class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # Boyer-Moore Voting Algorithm
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        res = 0 
        count = 0

        for num in nums:
            if count == 0:
                res = num

            count += (1 if num == res else -1)

        return res


        # hashmap = {}
        # res = 0
        # maxCount = 0

        # for num in nums:
        #     hashmap[num] = 1 + hashmap.get(num,0)
        #     res = num if hashmap[num] > maxCount else res

        #     maxCount = max(res, hashmap[num])
        # return res
            
        