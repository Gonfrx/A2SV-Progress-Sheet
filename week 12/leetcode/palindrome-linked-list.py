class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next: return True
        temp = head
        slow = head 
        fast = head
        
        while fast and fast.next:
            temp = slow
            slow = slow.next
            fast = fast.next.next
        
        cotemp = temp
        coslow = slow
        temp = slow
        n = slow
        while n: 
            n = slow.next
            slow.next = temp
            temp = slow
            slow = n
        coslow.next = None
        cotemp.next = temp
        h = temp

        while temp and not head == h:
            if not head.val == temp.val: return False
            head = head.next
            temp = temp.next
        
        return True
        