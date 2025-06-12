class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l = 0
        r = len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum == target:
                return [l+1, r+1]

            elif curSum > target:
                r -=1
            else:
                l += 1
                
        return []
        
        # Time Complexity: O(n) 
        # Space Complexity: O(1) as we only use two pointers