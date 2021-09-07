# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 23:30:02 2021

@author: Evgeniya Vorontsova

LC Problem 83 Remove Duplicates from Sorted List

Given the head of a sorted linked list, delete all duplicates such that 
each element appears only once. Return the linked list sorted as well.

Example 1:

Input: head = [1,1,2]
Output: [1,2]

Example 2:

Input: head = [1,1,2,3,3]
Output: [1,2,3]

Constraints:

    The number of nodes in the list is in the range [0, 300].
    -100 <= Node.val <= 100
    The list is guaranteed to be sorted in ascending order.
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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p_list = head
        
        p_l_prev = None
        while p_list:
            if p_l_prev:
                if p_l_prev.val == p_list.val:
                    p_l_prev.next = p_list.next
                else:
                    p_l_prev = p_list
            else:     
                p_l_prev = p_list
            p_list = p_list.next    
            
            #head.print_list()  
        return head
             
# Tests
a = ListNode(1)
b = ListNode(1)
c = ListNode(2)
d = ListNode(2)
a.next = b
b.next = c
c.next = d
print("List: ")
a.print_list()

class_instance = Solution()
rez = Solution.deleteDuplicates(class_instance, a)
print("After processing:")
if rez:
    rez.print_list()             
