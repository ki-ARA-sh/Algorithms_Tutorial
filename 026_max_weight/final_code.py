n, m = map(int, input().split())
# Input
weight = []
for i in range(n):
    row = map(int, input().split())
    # weight.append(list(row))
    weight.insert(0, list(row))
# Create DP Table (2D,n*m)
dp = [[0 for x in range(m)] for x in range(n)]
# A table to make path
way = [['' for x in range(m)] for x in range(n)]
# Base Value

for i in range(n):
    for j in range(m):
        # Base Value
        if i == 0 and j == 0:
            dp[0][0] = weight[0][0]
            continue
        # Update DP
        downPath = leftPath = float('-inf')
        # if j==0 then [n][j] will be out of table
        if i != 0:
            downPath = dp[i-1][j]
        # if j==0 then [i+1][-1] will be out of table
        if j != 0:
            leftPath = dp[i][j-1]
        # Update DP and specify which direction should be store in 'way'
        if leftPath > downPath:
            way[i][j] = 'R'
            dp[i][j] = leftPath+weight[i][j]
        else:
            way[i][j] = 'U'
            dp[i][j] = downPath+weight[i][j]

# Maximum weight
print(dp[n-1][m-1])
# Make path by 'way'
path = ''
row, col = n-1, m-1
for i in range(n+m-2):
    cur=way[row][col]
    #Current direction
    path=cur+path
    if cur=='R':
        col-=1
    else:
        row-=1
print(path)