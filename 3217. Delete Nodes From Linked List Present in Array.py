# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        num_set = set(nums)
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy

        while curr and curr.next:
            if curr.next.val in num_set:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next
