class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0       # Initialize the current subarray sum to 0
        maxSum = nums[0]  # Initialize the maximum sum to the first element of the array

        for num in nums:   # Iterate over each number in the input array
            if curSum < 0: # if curSum is negative
                curSum = 0  # Reset curSum as a negative curSum would only make any subsequent subarray's sum smaller
            
            curSum += num  # Add the current number to the curSum
            maxSum = max(curSum, maxSum) # Update maxSum if curSum is greater
        return maxSum #return the max sum of any contiguous subarray