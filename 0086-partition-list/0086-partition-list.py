# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        new1 = ListNode(0)
        new2 = ListNode(0)
        temp1 = new1
        temp2 = new2
        curr = head
        while curr:
            if curr.val < x :
                temp1.next = curr
                temp1 = temp1.next
                curr = curr.next
            else:
                temp2.next = curr
                temp2 = temp2.next
                curr = curr.next
        temp2.next = None
        temp1.next = new2.next

        return new1.next
