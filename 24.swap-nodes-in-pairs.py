#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0, head)
        tail = head
        while (tail.next and tail.next.next):
            p = tail.next
            q = tail.next.next

            p.next = q.next
            q.next = p
            tail.next = q
            tail = p
        return head.next




# @lc code=end

