class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = ListNode()
        h = less
        greater = ListNode()
        h2 = greater
        curr = head
    
        while(curr):
            temp = ListNode(curr.val)
            if curr.val < x:
                less.next = temp
                less = less.next
            else:
                greater.next = temp
                greater = greater.next
            curr = curr.next
        
        less.next = h2.next
        return h.next