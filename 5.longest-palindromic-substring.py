#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(s, i, j):
            while i >= 0 and j < len(s) and s[i]==s[j]:
                i-=1
                j+=1
            return (i+1, j)

        derp = (0, 0)
        for i in range(len(s)):
            derp = max(expand(s,i,i), expand(s,i,i+1), derp, key=lambda x: x[1]-x[0])
        return s[derp[0]:derp[1]]
# @lc code=end

