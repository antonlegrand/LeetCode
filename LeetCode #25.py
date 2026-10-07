"""
25. Reverse Nodes in k-Group
Hard
Topics
premium lock icon
Companies
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while True:
            count = 0
            node = current
            while count < k and node.next:
                node = node.next
                count += 1

            if count < k:
                break

            prev = None
            curr = current.next
            for _ in range(k):
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node

            tail = current.next
            tail.next = curr
            current.next = prev
            current = tail

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
    list_1 = build_list([1, 2, 3, 4, 5])
    k = 2
    result = Solution().reverseKGroup(list_1, k)
    print(to_list(result))  # Output: [2, 1, 4, 3, 5]

    list_2 = build_list([1, 2, 3, 4, 5])
    k = 3
    result = Solution().reverseKGroup(list_2, k)
    print(to_list(result))  # Output: [3, 2, 1, 4, 5]