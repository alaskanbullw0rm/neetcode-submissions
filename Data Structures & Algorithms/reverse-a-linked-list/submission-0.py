# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newNode = None
        while head:
            newNode = ListNode(head.val, newNode)
            head = head.next
        return newNode
        