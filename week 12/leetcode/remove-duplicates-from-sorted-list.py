class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = [-101]
        curr = head
        while curr:
            if not nums[-1] == curr.val:
                nums.append(curr.val)
            curr= curr.next
            
        dummy = ListNode(0)
        c = dummy
        for i in range(1, len(nums)):
            temp = ListNode(nums[i])
            c.next = temp
            c = c.next
        return dummy.next