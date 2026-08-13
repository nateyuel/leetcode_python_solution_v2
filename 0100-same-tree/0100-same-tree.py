# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    
        def helper(root):
            if not root:
                return [None]

            arr = []
            queue = deque([root])
            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()

                    if node:
                        arr.append(node.val)
                        queue.append(node.left)
                        queue.append(node.right)
                    else:
                        arr.append(None)

            return arr
        
        arr_p = helper(p)
        arr_q = helper(q)
        
        return arr_p == arr_q
        