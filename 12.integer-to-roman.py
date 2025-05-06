#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        out = ""

        place_value = 3
        ones = ["I", "X", "C", "M"]
        fives = ["V", "L", "D", ""]
        div = [1, 10, 100, 1000]

        while (place_value>= 0):
            dig = (num // div[place_value]) % 10
            if (dig == 4):
                out += ''.join([ones[place_value], fives[place_value]])
            elif (dig==9):
                out += ''.join([ones[place_value], ones[place_value+1]])
            else:
                if (dig>=5):
                    out += fives[place_value]
                    dig -= 5
                out += ''.join([ones[place_value] for _ in range(dig)])
            place_value -= 1
        return out




# @lc code=end

