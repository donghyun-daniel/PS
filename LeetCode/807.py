class Solution:
    def maxIncreaseKeepingSkyline(self, grid)->int:
        row = [max(row) for row in grid]
        col = [max(col) for col in zip(*grid)]
        ans=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans+=min(row[i],col[j])-grid[i][j]
        return ans

print(Solution.maxIncreaseKeepingSkyline(None,[[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]))