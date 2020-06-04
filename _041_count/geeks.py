# Python3 implementation of the above approach
from bisect import bisect as upper_bound

maxLen = 30


# Function to find required value
def findCnt(arr, n, k):
    # Variable to store final answer
    ans = 0

    # Loop to find prefix-sum
    for i in range(1, n):
        arr[i] += arr[i - 1]
        if (arr[i] > k or arr[i] < -1 * k):
            ans += 1

    if (arr[0] > k or arr[0] < -1 * k):
        ans += 1

    # Sorting prefix-sum array
    arr = sorted(arr)

    # Loop to find upper_bound
    # for each element
    for i in range(n):
        ans += n - upper_bound(arr, arr[i] + k)

        # Returning final answer
    return ans


# Driver code

arr = [-1, 4, -5, 6]
n = len(arr)
k = 0

# Function to find required value
print(findCnt(arr, n, k))

# This code is contributed by mohit kumar 29
