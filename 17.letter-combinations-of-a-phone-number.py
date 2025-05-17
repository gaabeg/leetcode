#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start

from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_dig = len(digits)
        if num_dig == 0:
            return []
        dp = [[] for _ in range(num_dig + 1)]
        dp[0] = [""]
        dict = {
           "2":["a","b","c"],
           "3":["d","e","f"],
           "4":["g","h","i"],
           "5":["j","k","l"],
           "6":["m","n","o"],
           "7":["p","q","r", "s"],
           "8":["t","u","v"],
           "9":["w","x","y", "z"]
        }
        for i in range(num_dig):
           cur_dig = digits[i]
           for prev in dp[i]:
               for new in dict[cur_dig]:
                   dp[i+1].append(prev + new)
        
        return dp[num_dig]


# @lc code=end

