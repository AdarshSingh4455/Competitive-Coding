class Solution:
    def oddEvenList(self, head):
        # Handle edge cases: if list is empty or has only one node
        if not head or not head.next:
            return head
        
        odd = head
        even = head.next
        evenHead = even # store even head to connect later
        
        while even and even.next:
            odd.next = odd.next.next     # link odd nodes
            odd = odd.next               # move odd pointer
            even.next = even.next.next   # link even nodes
            even = even.next             # move even pointer
            
        odd.next = evenHead # connect odd chain with even chain
        return head
