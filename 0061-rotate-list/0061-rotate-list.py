class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        
        if not head or not head.next or k == 0:
            return head
        length = 1
        temp = head

        while temp.next:
            temp = temp.next
            length += 1
        k = k % length

        if k == 0:
            return head
        temp.next = head
        steps = length - k
        new_tail = head

        for _ in range(steps - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None

        return new_head