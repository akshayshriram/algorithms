# The 2D Kadane's Algorithm => Maximum Sum Submatrix problem, 
# It extends the original 1D Kadane's algorithm by reducing the 2D problem into a series of 1D maximum subarray problems.

# Time Complexity: The time complexity is (O(N X M^{2})), Where (N) is the number of rows and (M) is the number of columns.
# The outer loops to fix the left and right columns run in (O(M^{2})) time.
# The inner loop for calculating the compressed row sums takes (O(N)) time.
# Applying the 1D Kadane's algorithm takes (O(N)) time.
# ====> (O(N) + O(N)) X (O(M^{2}))
# ====>(O(N X M^{2}))

# Space Complexity: The space complexity is \(O(N)\) to store the temporary 1D array of row sums.

import sys

def kanadeAlgorithm(givenArray):
    currentSum = givenArray[0]
    maxSum = -sys.maxsize - 1
    
    for i in range(1,len(givenArray)):
        if currentSum + givenArray[i] > givenArray[i]:
            currentSum = currentSum + givenArray[i]           
        else:
            currentSum = givenArray[i]
        maxSum = max(currentSum, maxSum)
    
    return maxSum


matrix = [[1, 2, -1, -4, -20],[-8, -3, 4, 2, 1],[3, 8, 10, 1, 3],[-4, -1, 1, 7, -6]]

n = len(matrix)
m = len(matrix[0])
ans = -sys.maxsize - 1
for i in range(len(matrix)):
    temp = []
    for j in range(n):
        temp.append(matrix[j][i])
    print(temp)
    ans = max(ans,kanadeAlgorithm(temp))
    print(ans)
    print("------------")
    for j in range(i+1,len(matrix)):
        for k in range(n):
            temp[k] += matrix[k][j]
        print(temp)
        ans = max(ans,kanadeAlgorithm(temp))
        print("========")
                
print(ans)