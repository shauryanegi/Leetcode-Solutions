class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        sum_nums = sum(nums) # O(n)
        left_sum = 0
        for index, num in enumerate(nums):
            right_sum = sum_nums - left_sum - num
            if left_sum == right_sum:
                return index
            left_sum += num
        return -1

        