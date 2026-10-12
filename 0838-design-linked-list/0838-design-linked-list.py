
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        curr = self.head
        count = 0

        while curr:
            if index == count:
                return curr.val
            curr = curr.next
            count += 1

        return -1

    def addAtHead(self, val: int) -> None:
        new_node = MyLinkedListNode(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = MyLinkedListNode(val)

        if self.head is None:
            self.head = new_node
            self.size += 1
            return

        curr = self.head
        while curr.next is not None:
            curr = curr.next

        curr.next = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
            return

        new_node = MyLinkedListNode(val)
        curr = self.head
        count = 0

        while curr:
            if count + 1 == index:
                new_node.next = curr.next
                curr.next = new_node
                self.size += 1
                return

            curr = curr.next
            count += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return

        curr = self.head
        count = 0

        while curr.next:
            if count + 1 == index:
                curr.next = curr.next.next
                self.size -= 1
                return

            curr = curr.next
            count += 1


class MyLinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# LeetCode usage:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index, val)
# obj.deleteAtIndex(index)
