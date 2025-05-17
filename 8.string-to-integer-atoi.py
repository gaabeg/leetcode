#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        num = 0
        lead = True
        sign = 1
        MAX_INT = 2**31 - 1
        MIN_INT = -1*(2**31)
        for char in s:
            if lead:
                if char==' ':
                    continue
                if char=='+':
                    lead = False
                    continue
                if char=='-':
                    lead = False
                    sign = -1
                    continue
            if char.isdigit():
                lead = False
                new_num = int(char)
                if sign==1 and num > (MAX_INT - new_num)/10.0:
                    return MAX_INT
                elif sign==-1 and -1*num < (MIN_INT+new_num)/(10.0):
                    return MIN_INT
                num = num*10 + new_num
                continue
            break
        return sign*num
# @lc code=end

