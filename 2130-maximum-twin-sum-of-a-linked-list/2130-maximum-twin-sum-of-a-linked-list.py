# Definition for singly-linked list.
# class Listhead:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[Listhead]) -> int:
        store = []

        while head.next:
            store.append(head.val)
            head = head.next

        store.append(head.val)
        n = len(store)

        for i in range((n//2), n):
            store[abs(i+1-n)] += store[i]

        return max(store)