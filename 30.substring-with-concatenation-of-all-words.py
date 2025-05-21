#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#

# @lc code=start
from typing import List
import copy
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordLen = len(words[0])
        if len(set(words)) == 1:
            check_sub = words[0]*len(words)
            i, indices = 0, []
            while (i <= len(s)-len(check_sub)):
                if (s[i:i+len(check_sub)] == check_sub):
                    indices.append(i)
                i+=1
            return indices





        def check_from_spot(idx, lilslice):
            curWords = copy.deepcopy(words)
            curWords.remove(lilslice)
            while curWords:
                slice = s[idx: idx+wordLen]
                if slice in curWords:
                   curWords.remove(slice)
                   idx+=wordLen
                else:
                   return False
            return True
        i = 0
        indices = []
        while (i <= len(s)-(wordLen*len(words))):
            slice = s[i:i+wordLen]
            if (slice in words and check_from_spot(i+wordLen, slice)):
                indices.append(i)
            i+=1
        return indices      
           

# @lc code=end

