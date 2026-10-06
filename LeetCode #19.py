"""
Exercice 19


Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 
"""


# Definition for singly-linked list.
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        # Avance fast de n pas
        for _ in range(n):
            fast = fast.next

        # Avance les deux pointeurs jusqu'à ce que fast atteigne le dernier noeud
        while fast.next is not None:
            fast = fast.next
            slow = slow.next

        # slow est juste avant le noeud à supprimer
        slow.next = slow.next.next
        return dummy.next


def build_list(values):
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


if __name__ == "__main__":
    head = build_list([1, 2, 3, 4, 5])
    result = Solution().removeNthFromEnd(head, 2)
    print(to_list(result))  # [1, 2, 3, 5]
