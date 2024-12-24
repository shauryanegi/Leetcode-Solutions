class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        # return []

        prevMap = {}  #value:index

        for index, number in enumerate(nums):
            diff = target - number

            if diff in prevMap:
                return [prevMap[diff], index]

            prevMap[number] = index

        return


# O(n) time complexity
# O(n) space complexity


        