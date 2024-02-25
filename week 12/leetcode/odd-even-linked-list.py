class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        if not head.next: return head
    
        odd, even = head, head
        even = second = head.next
        while odd and even.next: 
            odd.next = even.next
            odd = odd.next
            if odd.next:
                even.next = odd.next
                even = even.next
            else: break
        
        even.next = None
        odd.next = second
        return head