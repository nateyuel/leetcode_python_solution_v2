# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count_nodes = 1
        node = head

        if not head:
            return head

        while node.next:
            node = node.next
            count_nodes += 1
        
        fin_rot = k % count_nodes

        if fin_rot == 0:
            return head

        break_node = count_nodes - fin_rot

        curr_node = head
        res = head
        while break_node > 0:
            if break_node == 1:
                res = curr_node.next
                curr_node.next = None
            else:
                curr_node = curr_node.next

            break_node -= 1
        
        node.next = head

        return res



        
        

