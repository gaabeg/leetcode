#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List, Optional
class Solution:
    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     if len(lists)==0:
    #         return None
    #     elif len(lists) == 1:
    #         return lists[0]
    #     head = lists[0]
    #     for idx in range(1, len(lists)):
    #         if head == None:
    #             head = lists[idx]
    #             continue
    #         if lists[idx] == None:
    #             continue
    #         if (head.val<lists[idx].val):
    #             i,j = head, lists[idx]
    #         else:
    #             i,j = lists[idx], head
    #         head = i
    #         while(i.next and j):
    #             if (j.val <= i.next.val):
    #                 temp = j.next
    #                 j.next = i.next
    #                 i.next = j
    #                 j = temp
    #             i = i.next
    #         if (i.next == None):
    #             i.next = j
    #     return head


    def merge(self, list1, list2):
        if (not list1):
            return list2
        elif (not list2):
            return list1
        head = ListNode()
        tail = head
        while (list1 and list2):
            if (list1.val<=list2.val):
                tail.next = list1
                tail = tail.next
                list1 = list1.next
            else:
                tail.next = list2
                tail = tail.next
                list2 = list2.next
        if (not list1):
            tail.next = list2
        elif (not list2):
            tail.next = list1
        return head.next
    

    def divide(self, lists, p, q):
        if q<=p:
            return lists[p]
        mid =p +( (q-p) // 2)
        return self.merge(self.divide(lists, p, mid), self.divide(lists,mid+1,q))
    

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        return self.divide(lists, 0, len(lists)-1)


    



# @lc code=end

