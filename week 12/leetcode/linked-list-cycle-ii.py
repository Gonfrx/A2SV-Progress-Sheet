class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        flag = False
        if not head:
            return None
        
        while(fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                flag = True
                break
        
        if flag == False:
            return None
        
        while slow:
            if head == slow: 
                return slow
            head = head.next
            slow = slow.next
        
        return None