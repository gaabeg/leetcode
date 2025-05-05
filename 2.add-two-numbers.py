#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#      def __init__(self, val=0, next=None):
#          self.val = val
#          self.next = next
from typing import Optional


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = int(l1.val + l2.val) // 10
        first = ListNode(int(l1.val + l2.val) % 10)
        curr = first
        while (l1.next != None and l2.next != None):
            curr.next = ListNode()
            curr = curr.next            
            l1 = l1.next
            l2 = l2.next
            curr.val = int(l1.val + l2.val + carry) % 10
            carry = int(l1.val + l2.val + carry) // 10
        while (l1.next == None and l2.next !=None):
            curr.next = ListNode()
            curr = curr.next            
            l2 = l2.next
            curr.val = int(l2.val + carry) % 10
            carry = int(l2.val + carry) // 10
        while (l2.next == None and l1.next !=None):
            curr.next = ListNode()
            curr = curr.next            
            l1 = l1.next
            curr.val = int(l1.val + carry) % 10
            carry = int(l1.val + carry) // 10
        if (carry != 0):
            curr.next = ListNode(carry)
        print(type(first))
        return first

            
# @lc code=end