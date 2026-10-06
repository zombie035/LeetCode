class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:

        # 1. Check whether there are k nodes available
        curr = head
        count = 0

        while curr and count < k:
            curr = curr.next
            count += 1

        # Less than k nodes â don't reverse
        if count < k:
            return head

        # 2. Reverse exactly k nodes
        prev = None
        curr = head

        for _ in range(k):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # 3. head is now the last node of the reversed group
        # Connect it to the recursively reversed remaining list
        head.next = self.reverseKGroup(curr, k)

        # 4. prev is the new head of this reversed group
        return prev