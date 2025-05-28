# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def doubleIt(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Step 1: Reverse the linked list
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        head = prev  # New head after reversal

        # Step 2: Double the value and handle carry
        curr = head
        carry = 0
        while curr:
            doubled = curr.val * 2 + carry
            curr.val = doubled % 10
            carry = doubled // 10
            if not curr.next and carry:
                curr.next = ListNode(0)  # Extend list if needed
            curr = curr.next

        # Step 3: Reverse the list again to restore original order
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev  # Final head of the updated list

        
