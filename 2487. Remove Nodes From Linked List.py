# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def reverse(head):
            prev = None
            while head:
                next_node = head.next
                head.next = prev
                prev = head
                head = next_node
            return prev
        
        head = reverse(head)
        max_value = head.val
        curr = head

        while curr and curr.next:
            if curr.next.val < max_value:
                curr.next = curr.next.next
            else:
                curr = curr.next
                max_value = curr.val
        
        return reverse(head)
