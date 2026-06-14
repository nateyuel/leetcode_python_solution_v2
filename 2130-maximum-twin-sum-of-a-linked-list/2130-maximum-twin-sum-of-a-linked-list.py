# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        n = 1
        node = head

        while node.next:
            node = node.next
            n += 1
        
        max_twin_sum = 0
        store = []

        curr = head
        for i in range(n):
            if i <= (n / 2) - 1:
                store.append(curr.val)
            else:
                j = abs(i+1-n)
                store[j] += curr.val
                max_twin_sum = max(max_twin_sum, store[j])

            if curr.next:
                curr = curr.next
        
        return max_twin_sum
