# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        h, prev, temp = head, head, head
        
        while temp.next:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        head.next = prev
        h.next = None
        return head
        