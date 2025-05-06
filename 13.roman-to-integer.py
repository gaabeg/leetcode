#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        letters = ["I", "V", "X", "L", "C", "D", "M", "", ""]
        nums = [1, 5, 10, 50, 100, 500, 1000]
        tot, i = 0, 0
        while (i < len(s)):
            ind = letters.index(s[i])
            if (i + 1 < len(s) and s[i+1] == letters[ind+1]):
                tot += (nums[ind]*4)
                i+= 2
            elif (i + 1 < len(s) and s[i+1] == letters[ind+2]):
                tot += (nums[ind]*9)
                i+=2
            else: 
                tot += nums[ind]
                i+=1
        return tot

# @lc code=end

