# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    
        def helper(node):
            if not node:
                return [None]

            arr = []
            queue = deque([node])
            while queue:
                for _ in range(len(queue)):
                    poped = queue.popleft()

                    if poped:
                        arr.append(poped.val)
                        queue.append(poped.left)
                        queue.append(poped.right)
                    else:
                        arr.append(None)

            return arr
        
        arr_p = helper(p)
        arr_q = helper(q)
        
        return arr_p == arr_q
        