"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, 
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 
Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy_head.next
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        values = []
        current = self

        while current:
            values.append(str(current.val))
            current = current.next

        return " -> ".join(values) + " -> None"
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy_head.next

    
def to_linked_list(nums):
    if not nums:
        return None
    head = ListNode(nums[0])
    cur = head
    for x in nums[1:]:
        cur.next = ListNode(x)
        cur = cur.next
    return head


# Tests
l1 = to_linked_list([2, 4, 3])  # représente 342
l2 = to_linked_list([5, 6, 4])  # représente 465

sol = Solution()
res = sol.addTwoNumbers(l1, l2)

print("l1 :", l1)          # 2 -> 4 -> 3
print("l2 :", l2)          # 5 -> 6 -> 4
print("résultat :", res)   # 7 -> 0 -> 8  (car 342 + 465 = 807)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(0)
    curr = dummy
    carry = 0

    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        s = v1 + v2 + carry
        curr.next = ListNode(s % 10)
        carry = s // 10

        curr = curr.next
        if l1: l1 = l1.next
        if l2: l2 = l2.next

    return dummy.next


def build_list(values):
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def list_to_array(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

# Test avec ton input
l1 = build_list([2, 4, 3])
l2 = build_list([5, 6, 4])

result = addTwoNumbers(l1, l2)

print(list_to_array(result))  # -> [7, 0, 8]