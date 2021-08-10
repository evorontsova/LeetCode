# -*- coding: utf-8 -*-
"""
LC Problem 21 Merge Two Sorted Lists

Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

Example 1:
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: l1 = [], l2 = []
Output: []

Example 3:

Input: l1 = [], l2 = [0]
Output: [0]


Constraints:

    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
"""

from typing import Optional 

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
     
     def print_list(self):
         p = self
         while True:
             print(p.val, end='')
             p = p.next
             if not p:
                 break
             else:
                 print("--> ", end='')
         print()
                
class Solution:
    
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        p_l1_prev = None
        
        if l1:
            p_l1_cur = l1
        else:
            return l2
        
        p_l2 = l2
        
        if not p_l2:
            return l1
        
        if p_l1_cur.val > p_l2.val:
            head = p_l2
        else:
            head = p_l1_cur
            
        while p_l1_cur:
            while p_l2.val < p_l1_cur.val:
                if p_l1_prev:
                    p_l1_prev.next = p_l2
                p_l1_prev = p_l2
                
                if p_l2.next:
                    tmp = p_l2.next
                    p_l2.next = p_l1_cur    
                    p_l2 = tmp
                else:
                    p_l2.next = p_l1_cur
                    return head
            
            p_l1_prev = p_l1_cur
            if p_l1_cur.next:
                p_l1_cur = p_l1_cur.next       
            else:
                p_l1_cur = None
            
     
            #head.print_list()
            #print("p_l1_cur = ", p_l1_cur.val, ", p_l1_prev = ", p_l1_prev.val, ", p_l2 = ", p_l2.val)
            
        if p_l2:
            p_l1_prev.next = p_l2
            
        return head
        
    
# Tests
a = ListNode(1)
b = ListNode(2)
c = ListNode(4)
#d = ListNode(12)
a.next = b
b.next = c
#c.next = d
print("List 1: ")
a.print_list()

aa = ListNode(1)
bb = ListNode(3)
a1 = ListNode(4)
#b1 = ListNode(8)
#c1 = ListNode(10)
#d1 = ListNode(15)
aa.next = bb
bb.next = a1
#a1.next = b1
#b1.next = c1
#c1.next = d1
print("List 2: ")
aa.print_list()

class_instance = Solution()
rez = Solution.mergeTwoLists(class_instance, a, aa)
print("Merged list:")
if rez:
    rez.print_list() 
        
