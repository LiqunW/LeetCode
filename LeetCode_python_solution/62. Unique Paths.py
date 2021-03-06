'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28

题意：机器人只能往下和往右走，问一共有多少中走法可以从左上角到右下角
思路：动态规划的思想，走到边上的格子只有一种走法，a[i][j]=a[i-1][j]+a[i][j-1]
'''

class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        path=[[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 or j ==0:
                    path[i][j]=1
                else:
                    path[i][j]=path[i][j-1]+path[i-1][j]
        return path[-1][-1]