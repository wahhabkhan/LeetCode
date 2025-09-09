# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next or k == 0:
            return head

        # 1. Count length & get tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # 2. Adjust k
        k %= length
        if k == 0:
            return head

        # 3. Make it circular
        tail.next = head

        # 4. Find new tail: (length - k - 1) steps
        steps_to_new_tail = length - k
        new_tail = head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next

        # 5. Break circle
        new_head = new_tail.next
        new_tail.next = None

        return new_head
