# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        critical_points = []
        k = 1
        curr_node = head

        while curr_node.next and curr_node.next.next:
            prev_node = curr_node
            curr_node = curr_node.next
            next_node = curr_node.next
            
            if (curr_node.val > prev_node.val and curr_node.val > next_node.val) or (curr_node.val < prev_node.val and curr_node.val < next_node.val):
                critical_points.append(k)

            k += 1

        result = [-1, -1]
        length = len(critical_points)
        if length >= 2:
            min_dist = float("inf")
            for idx in range(1, length):
                min_dist = min(min_dist, critical_points[idx] - critical_points[idx-1])
            
            result[0] = min_dist
            result[1] = critical_points[-1] - critical_points[0]

        return result

            
