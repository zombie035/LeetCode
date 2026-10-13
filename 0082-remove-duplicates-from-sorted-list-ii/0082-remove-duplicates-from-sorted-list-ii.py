class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        while curr.next and curr.next.next:
            if curr.next.val == curr.next.next.val:
                duplicate = curr.next.val
                while curr.next and curr.next.val == duplicate:
                    curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next