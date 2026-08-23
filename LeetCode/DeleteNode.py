# Write a function to delete a given node from a singly linked list when only
# that node is provided. The node is guaranteed not to be the tail node....Q-237

class Solution(object):
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next