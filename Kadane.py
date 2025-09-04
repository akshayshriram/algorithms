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
    