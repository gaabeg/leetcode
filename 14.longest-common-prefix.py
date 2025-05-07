#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = strs[0]
        for idx in range(1, len(strs)):
            if pref == "":
                return pref
            found = False
            while (not found): 
                if (strs[idx].startswith(pref)):
                    found = True
                else:
                    pref = pref[:len(pref)-1]
        return pref
# @lc code=end

