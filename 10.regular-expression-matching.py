#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p) 
        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[0][0] = True
        for j in range(2, n+1):
            if p[j-1] == "*":
                dp[0][j] = dp[0][j-2]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1]=="*":
                    matchPrev = dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2]==".")
                    empty = dp[i][j-2]
                    dp[i][j] = empty or matchPrev 
                else:
                    dp[i][j] = dp[i-1][j-1] and (s[i-1]==p[j-1] or p[j-1]==".")
        return dp[m][n]

            

            



# @lc code=end

