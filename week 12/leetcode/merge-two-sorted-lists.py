class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = ListNode(0)
        dummy = curr 
        u = list1
        d = list2
        def rec(u, d, dummy):
            if u and d:
                if u.val <= d.val: 
                    temp = ListNode(u.val)
                    dummy.next = temp
                    dummy = dummy.next
                    return rec(u.next, d,dummy)
                else:
                    temp = ListNode(d.val)
                    dummy.next = temp
                    dummy = dummy.next
                    return rec(u, d.next,dummy) 
            elif u:
                temp = ListNode(u.val)
                dummy.next = temp
                dummy = dummy.next
                return rec(u.next, d,dummy)
            elif d:
                temp = ListNode(d.val)
                dummy.next = temp
                dummy = dummy.next
                return rec(u, d.next,dummy)
            else:
                return curr.next 
                 
        
        return rec(u, d,dummy)

        