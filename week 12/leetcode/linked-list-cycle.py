class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        n = head
        while not n == None and not n.next == None:
            head = head.next
            n = n.next.next
            if head == n: 
                return True

        return False 