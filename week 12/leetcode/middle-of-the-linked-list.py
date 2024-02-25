class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while(fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next

        if fast.next:
            return slow.next
        return slow 
        
