# Kadane's Algorithm => "Maximum Subarray Problem." 
# This problem involves finding the contiguous subarray within a one-dimensional array of numbers that has the largest sum
# Time Complexity: O(N), as the algorithm iterates through the array only once.
# Space Complexity: O(1), as it uses a constant amount of extra space for variables. 


nums = [1]

currentSum = nums[0]
overallSum = nums[0]

for i in range(1,len(nums)):
    if len(nums) == 0:
        currentSum, overallSum = nums[i]
        break
    if currentSum + nums[i] > nums[i]:
        currentSum = currentSum + nums[i]
    else:
        currentSum = nums[i]
    overallSum = max(currentSum, overallSum)

print(overallSum)
    