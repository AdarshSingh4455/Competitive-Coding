class Solution:
    def reorderList(self, head):
        slow = head
        fast = head

        if not head or not head.next:
            return

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        current = slow.next
        first = head
        slow.next = None

        prev = None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        second = prev

        while first and second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next