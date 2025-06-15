class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        hashmap = {}
        res = []

        for index,number in enumerate(sorted_nums):
            if number not in hashmap:
                hashmap[number] = index

        for index in nums:
            res.append(hashmap[index])

        return res


