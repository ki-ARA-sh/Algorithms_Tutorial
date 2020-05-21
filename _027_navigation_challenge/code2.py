n, m = map(int, input().split())
# Input
weight = []
for i in range(n):
    row = map(int, input().split())
    weight.append(list(row))
# Create DP Table (2D,n*m)
dp = [[0 for x in range(m)] for x in range(n)]
prev_dir = [['' for x in range(m)] for x in range(n)]

for i in range(n):
    for j in range(m):
        # Base Value
        if i == 0 and j == 0:
            dp[0][0] = weight[0][0]
            continue
        # Update DP
        downPath = leftPath = rightPath = float('inf')
        prev_down = prev_left = prev_right = ''
        if i != 0:
            downPath = dp[i-1][j]
            # prev_down = prev_dir[i-1][j]
        if j != 0 and prev_dir[i][j-1] != 'L':
            rightPath = dp[i][j-1]
            # prev_right = prev_dir[i][j-1]
        if j != m - 1 and prev_dir[i][j+1] != 'R':
            leftPath = dp[i][j+1]
            # prev_left = prev_dir[i][j+1]
        if rightPath < downPath and rightPath < leftPath:
            dp[i][j] = rightPath + weight[i][j]
            prev_dir[i][j] = 'R'
        elif downPath < rightPath and downPath < leftPath:
            dp[i][j] = downPath + weight[i][j]
            prev_dir[i][j] = 'D'
        else:
            dp[i][j] = leftPath + weight[i][j]
            prev_dir[i][j] = 'L'

# Maximum weight
print(dp[n-1][m-1])
