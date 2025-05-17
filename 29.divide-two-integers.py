#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        neg = (dividend < 0) is (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)

        quot = 0

        while (divisor <= dividend):
            sdiv, shift = divisor, 1
            while (sdiv <= dividend):
                dividend -= sdiv
                quot += shift
                sdiv = sdiv << 1
                shift = shift << 1

        return min(max(-2147483648, (quot if neg else -quot)), 2147483647)
# @lc code=end

