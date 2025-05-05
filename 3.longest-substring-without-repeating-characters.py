#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        largest = 0
        for i in range(len(s)):
            j = i+1
            occured = [s[i]]
            while (j < len(s)):
                if s[j] in occured:
                    break
                occured.append(s[j])
                j += 1
            largest = max(largest, j-i)
        return largest


# @lc code=end

