"""

24. Swap Nodes in Pairs
Medium
Topics
Companies
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

Example 1:

Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next and current.next.next:
            first = current.next
            second = current.next.next

            first.next = second.next
            second.next = first
            current.next = second

            current = first

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
    list_1 = build_list([1, 2, 3, 4])
    swapped_list_1 = Solution().swapPairs(list_1)
    print(to_list(swapped_list_1))  # Output: [2, 1, 4, 3]

    list_2 = build_list([])
    swapped_list_2 = Solution().swapPairs(list_2)
    print(to_list(swapped_list_2))  # Output: []

    list_3 = build_list([1])
    swapped_list_3 = Solution().swapPairs(list_3)
    print(to_list(swapped_list_3))  # Output: [1]

    list_4 = build_list([1, 2, 3])
    swapped_list_4 = Solution().swapPairs(list_4)
    print(to_list(swapped_list_4))  # Output: [2, 1, 3]