class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        len1 = len2 = 0
        curra = headA
        currb = headB
        while(curra): 
            len1 += 1
            curra = curra.next
        while(currb):
            len2 += 1
            currb = currb.next
        
        curra = headA
        currb = headB
        if len1 > len2: 
            while(len1 > len2):
                curra = curra.next
                len1 -= 1
        if len2 > len1:
            while(len2 > len1):
                currb = currb.next
                len2 -= 1
        
        while(curra and currb):
            if curra == currb:
                return curra
            curra = curra.next
            currb = currb.next
        
        return None

        