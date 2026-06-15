# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        
        node = head
        n = 1

        while node.next:
            n += 1
            node = node.next
        
        m = n // 2

        if m == 0:
            return head.next
        
        curr = head

        while m > 0:
            if m == 1:
                curr.next = curr.next.next
            curr = curr.next

            m -= 1

        return head
            
