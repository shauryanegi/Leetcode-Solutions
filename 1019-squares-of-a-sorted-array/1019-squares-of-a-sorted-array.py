class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        L = 0
        R = len(nums) - 1
        result = []

        while L <= R:
            if abs(nums[L]) > abs(nums[R]):
                result.append(nums[L] ** 2)
                L += 1

            else:
                result.append(nums[R] ** 2)
                R -= 1
        
        result.reverse()

        return result

        