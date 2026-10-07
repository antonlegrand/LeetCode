"""
23. Merge k Sorted Lists
Hard
Topics
premium lock icon
Companies
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        import heapq

        min_heap = []
        for l in lists:
            while l:
                heapq.heappush(min_heap, l.val)
                l = l.next

        dummy = ListNode(0)
        current = dummy
        while min_heap:
            current.next = ListNode(heapq.heappop(min_heap))
            current = current.next

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
    list_1 = build_list([1,4,5])
    list_2 = build_list([1,3,4])
    list_3 = build_list([2,6])
    merged_list = Solution().mergeKLists([list_1, list_2, list_3])
    print(to_list(merged_list))  # [1,1,2,3,4,4,5,6]
