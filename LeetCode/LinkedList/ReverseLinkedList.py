# Question: Given the head of a singly linked list, reverse the list and
# return its new head.
class Solution:
    def reverseList(self, head):
        prev = None
        current = head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev